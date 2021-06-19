# Copyright 2019 The ROBEL Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Turn tasks with DClaw robots.

This is a single rotation of an object from an initial angle to a target angle.
"""

import abc
import collections
import pdb
from typing import Dict, Optional, Sequence

import numpy as np
from transforms3d.euler import euler2quat

from robel.components.robot.dynamixel_robot import DynamixelRobotState
from robel.dclaw.base_env import BaseDClawObjectEnv
from robel.simulation.randomize import SimRandomizer
from robel.utils.configurable import configurable
from robel.utils.resources import get_asset_path

# The observation keys that are concatenated as the environment observation.
# DEFAULT_OBSERVATION_KEYS = (
#     'claw_qpos',
#     'object_qpos',
#     'object_qvel',
#     'target_error',
# )
DEFAULT_OBSERVATION_KEYS = (
    'claw_qpos',
    'object_qpos',
    # 'object_qvel',
    'target_error',
)
TARGET_Z = 0.1

# Reset pose for the claw joints.
RESET_POSE = [0.3] + [0, -np.pi / 3, np.pi / 3] * 3

DCLAW3_ASSET_PATH = 'robel/dclaw/assets/turn_3.xml'


class BaseDClawTurn(BaseDClawObjectEnv, metaclass=abc.ABCMeta):
    """Shared logic for DClaw turn tasks."""

    def __init__(self,
                 asset_path: str = DCLAW3_ASSET_PATH,
                 observation_keys: Sequence[str] = DEFAULT_OBSERVATION_KEYS,
                 frame_skip: int = 40,
                 interactive: bool = False,
                 success_threshold: float = 0.03,
                 **kwargs):
        """Initializes the environment.

        Args:
            asset_path: The XML model file to load.
            observation_keys: The keys in `get_obs_dict` to concatenate as the
                observations returned by `step` and `reset`.
            frame_skip: The number of simulation steps per environment step.
            interactive: If True, allows the hardware guide motor to freely
                rotate and its current angle is used as the goal.
            success_threshold: The difference threshold (in radians) of the
                object position and the goal position within which we consider
                as a sucesss.
        """
        super().__init__(
            sim_model=get_asset_path(asset_path),
            observation_keys=observation_keys,
            frame_skip=frame_skip,
            free_object=False,
            **kwargs)

        self._interactive = interactive
        self._success_threshold = success_threshold
        self._desired_claw_pos = RESET_POSE

        self._target_bid = self.model.body_name2id('target')

        # The following are modified (possibly every reset) by subclasses.
        self._initial_object_pos = None
        self._initial_object_vel = None
        self._set_target_object_pos(TARGET_Z)
        object_id = asset_path[5]
        if object_id == "3" or object_id == "4":
            self.lift_thres = 0.02
        elif object_id == "0" or "1" or "2":
            self.lift_thres = 0.065
        else:
            raise ValueError("wrong object id")

    def _reset(self):
        """Resets the environment."""
        self._reset_dclaw_and_object(
            claw_pos=RESET_POSE,
            object_pos=self._initial_object_pos,
            object_vel=self._initial_object_vel,
            guide_pos=self._target_object_pos)

        # Disengage the motor.
        if self._interactive and self.robot.is_hardware:
            self.robot.set_motors_engaged('guide', False)

    def _step(self, action: np.ndarray):
        action = action[2:]
        """Applies an action to the robot."""
        self.robot.step({
            'dclaw': action,
            'guide': np.atleast_1d(self._target_object_pos),
        })

    def get_obs_dict(self) -> Dict[str, np.ndarray]:
        """Returns the current observation of the environment.

        Returns:
            A dictionary of observation values. This should be an ordered
            dictionary if `observation_keys` isn't set.
        """
        claw_state, object_state,  = self.robot.get_state(
            ['dclaw', 'object'])
        base_pos = self.data.get_body_xpos('payload')
        # object_pos = self.data.get_body_xpos('object')
        # import pdb
        # pdb.set_trace()
        object_error = base_pos[2] - object_state.qpos[0]
        object_error -= 0.2 # guarantee that the base is not too close to the object
        # object_error = np.linalg.norm(object_error)

        # print(base_pos - object_state.qpos[:3])
        # If in interactive mode, use the guide motor position as the goal.
        # if self._interactive:
        #     self._set_target_object_pos(guide_state.qpos)

        # Calculate the signed angle difference to the target in [-pi, pi].
        target_error = object_state.qpos[0] - self._target_object_pos
        if target_error > 0:
            target_error = 0
        
        output_qpos = np.concatenate((np.zeros(2), claw_state.qpos))
        output_obj_pos = np.concatenate((object_state.qpos, np.zeros(1)))
        # obs_dict = collections.OrderedDict((
        #     ('claw_qpos', claw_state.qpos),
        #     ('claw_qvel', claw_state.qvel),
        #     ('object_qpos', object_state.qpos),
        #     ('object_qvel', object_state.qvel),
        #     ('target_error', target_error),
        #     ('object_error', object_error),
        # ))
        obs_dict = collections.OrderedDict((
            ('claw_qpos', output_qpos),
            ('claw_qvel', claw_state.qvel),
            ('object_qpos', output_obj_pos),
            ('object_qvel', object_state.qvel),
            ('target_error', target_error),
            ('object_error', object_error),
        ))
        # Add hardware-specific state if present.
        if isinstance(claw_state, DynamixelRobotState):
            obs_dict['claw_current'] = claw_state.current
        return obs_dict

    def get_reward_dict(
            self,
            action: np.ndarray,
            obs_dict: Dict[str, np.ndarray],
    ) -> Dict[str, np.ndarray]:
        """Returns the reward for the given action and observation."""
        target_dist = np.abs(obs_dict['target_error'])
        object_error = np.abs(obs_dict['object_error'])
        # object_qpos = obs_dict['object_qpos'][:,2:]
        claw_vel = obs_dict['claw_qvel'][1:]
        reward_dict = collections.OrderedDict((
            # Penalty for distance away from goal.
            ('target_dist_cost', -500 * target_dist),
            # Penalty for difference with nomimal pose.
            # ('pose_diff_cost',
            #  -1 * np.linalg.norm(obs_dict['claw_qpos'] - self._desired_claw_pos)
            # ),
            # Penality for high velocities.
            ('joint_vel_cost',
             -1 * np.linalg.norm(claw_vel[np.abs(claw_vel) >= 0.5])),
            # ('base_diff_cost',
            #  -100 * np.linalg.norm(obs_dict['claw_qpos'][:,:2] - np.array([[0,0]]))
            # ),
            # Reward for close proximity with goal.
            # ('bonus_lift', 10 * (object_qpos[0,2] > self.lift_thres)),
            ('bonus_small', 10 * (target_dist < 0.12)),
            ('bonus_big', 100 * (target_dist < self._success_threshold)),
            
            # Reward to punish the distance between object and the base
            ('object_error', -100 * object_error),

        ))
        return reward_dict

    def get_score_dict(
            self,
            obs_dict: Dict[str, np.ndarray],
            reward_dict: Dict[str, np.ndarray],
    ) -> Dict[str, np.ndarray]:
        """Returns a standardized measure of success for the environment."""
        target_dist = np.abs(obs_dict['target_error'])
        claw_qpos = obs_dict['claw_qpos'][:,2:]
        score_dict = collections.OrderedDict((
            ('points', 1.0 - target_dist),
            ('success', target_dist < self._success_threshold),
        ))
        score_dict.update(
            self._get_safety_scores(
                pos=claw_qpos,
                vel=obs_dict['claw_qvel'],
                current=obs_dict.get('claw_current'),
            ))
        return score_dict

    def _set_target_object_pos(self, target_pos: float,
                               unbounded: bool = False):
        """Sets the goal angle to the given position."""
        self._target_object_pos = np.asarray(target_pos, dtype=np.float32)

        # Mark the target position in sim.
        # WARNING: euler2quat will mutate a passed numpy array.
        self.model.body_quat[self._target_bid] = euler2quat(
            0, 0, float(target_pos))
    # def get_done(
    #         self,
    #         obs_dict: Dict[str, np.ndarray],
    #         reward_dict: Dict[str, np.ndarray],
    # ) -> np.ndarray:
    #     print("i am here!")
    #     return np.zeros((3,3))
    


@configurable(pickleable=True)
class DClawGrabFixed(BaseDClawTurn):
    """Turns the object with a fixed initial and fixed target position."""

    def _reset(self):
        # Turn from 0 degrees to 180 degrees.
        self._initial_object_pos = None
        self._set_target_object_pos(TARGET_Z)
        super()._reset()

