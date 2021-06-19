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

"""Gym environment registration for DClaw environments."""

from numpy.random import f
from robel.utils.registration import register

#===============================================================================
# Pose tasks
#===============================================================================

# Default number of steps per episode.
_POSE_EPISODE_LEN = 80  # 80*20*2.5ms = 4s

register(
    env_id='DClawPoseFixed-v0',
    class_path='robel.dclaw.pose:DClawPoseFixed',
    max_episode_steps=_POSE_EPISODE_LEN)

register(
    env_id='DClawPoseRandom-v0',
    class_path='robel.dclaw.pose:DClawPoseRandom',
    max_episode_steps=_POSE_EPISODE_LEN)

register(
    env_id='DClawPoseRandomDynamics-v0',
    class_path='robel.dclaw.pose:DClawPoseRandomDynamics',
    max_episode_steps=_POSE_EPISODE_LEN)

#===============================================================================
# Turn tasks
#===============================================================================

# Default number of steps per episode.
_ORIGIN_TRUN_EPISODE_LEN = 40
_TURN_EPISODE_LEN = 40  # 40*40*2.5ms = 4s
# changed to 800 and 4
register(
    env_id='DClawTurnFixed-v0',
    class_path='robel.dclaw.turn:DClawTurnFixed',
    max_episode_steps=_ORIGIN_TRUN_EPISODE_LEN,
    )
register(
    env_id='DClawTurnFixedD0-v0',
    class_path='robel.dclaw.turn:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN,
    kwargs={'asset_path':'robel/dclaw/assets/turn_0.xml',
        'frame_skip':40,
        })
register(
    env_id='DClawTurnFixedD1-v0',
    class_path='robel.dclaw.turn:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN,
    kwargs={'asset_path':'robel/dclaw/assets/turn_1.xml',
            'frame_skip':40,
            })
register(
    env_id='DClawTurnFixedD2-v0',
    class_path='robel.dclaw.turn:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN,
    kwargs={'asset_path':'robel/dclaw/assets/turn_2.xml',
            'frame_skip':40,
            })
register(
    env_id='DClawTurnFixedD3-v0',
    class_path='robel.dclaw.turn:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN,
    kwargs={'asset_path':'robel/dclaw/assets/turn_3.xml',
            'frame_skip':40,
            })
register(
    env_id='DClawTurnFixedD4-v0',
    class_path='robel.dclaw.turn:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN,
    kwargs={'asset_path':'robel/dclaw/assets/turn_4.xml',
            'frame_skip':40,
            })
# register(
#     env_id='DClawTurnFixedF0-v0',
#     class_path='robel.dclaw.turn_fixed:DClawTurnFixed',
#     max_episode_steps=_TURN_EPISODE_LEN ,
#     kwargs={'asset_path':'robel/dclaw/assets/fixed_turn_0.xml',
#         'frame_skip':40,
#         })
# register(
#     env_id='DClawTurnFixedF1-v0',
#     class_path='robel.dclaw.turn_fixed:DClawTurnFixed',
#     max_episode_steps=_TURN_EPISODE_LEN ,
#     kwargs={'asset_path':'robel/dclaw/assets/fixed_turn_1.xml',
#             'frame_skip':40,
#             })
# register(
#     env_id='DClawTurnFixedF2-v0',
#     class_path='robel.dclaw.turn_fixed:DClawTurnFixed',
#     max_episode_steps=_TURN_EPISODE_LEN ,
#     kwargs={'asset_path':'robel/dclaw/assets/fixed_turn_2.xml',
#             'frame_skip':40,
#             })
# register(
#     env_id='DClawTurnFixedF3-v0',
#     class_path='robel.dclaw.turn_fixed:DClawTurnFixed',
#     max_episode_steps=_TURN_EPISODE_LEN,
#     kwargs={'asset_path':'robel/dclaw/assets/fixed_turn_3.xml',
#             'frame_skip':40,
#             })
# register(
#     env_id='DClawTurnFixedF4-v0',
#     class_path='robel.dclaw.turn_fixed:DClawTurnFixed',
#     max_episode_steps=_TURN_EPISODE_LEN,
#     kwargs={'asset_path':'robel/dclaw/assets/fixed_turn_4.xml',
#             'frame_skip':40,
#             })

register(
    env_id='DClawTurnFixedF0-v0',
    class_path='robel.dclaw.turn_fixed:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN * 2,
    kwargs={'asset_path':'robel/dclaw/assets/fixed_turn_0.xml',
        'frame_skip':20,
        })
register(
    env_id='DClawTurnFixedF1-v0',
    class_path='robel.dclaw.turn_fixed:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN * 2,
    kwargs={'asset_path':'robel/dclaw/assets/fixed_turn_1.xml',
            'frame_skip':20,
            })
register(
    env_id='DClawTurnFixedF2-v0',
    class_path='robel.dclaw.turn_fixed:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN * 2,
    kwargs={'asset_path':'robel/dclaw/assets/fixed_turn_2.xml',
            'frame_skip':20,
            })
register(
    env_id='DClawTurnFixedF3-v0',
    class_path='robel.dclaw.turn_fixed:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN * 2,
    kwargs={'asset_path':'robel/dclaw/assets/fixed_turn_3.xml',
            'frame_skip':20,
            })
register(
    env_id='DClawTurnFixedF4-v0',
    class_path='robel.dclaw.turn_fixed:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN * 2,
    kwargs={'asset_path':'robel/dclaw/assets/fixed_turn_4.xml',
            'frame_skip':20,
            })




register(
    env_id='DClawTurnFixedT0-v0',
    class_path='robel.dclaw.turn_tactile:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN ,
    kwargs={'asset_path':'robel/dclaw/assets/turn_0_tactile.xml',
        'frame_skip':40,
        })
register(
    env_id='DClawTurnFixedT1-v0',
    class_path='robel.dclaw.turn_tactile:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN ,
    kwargs={'asset_path':'robel/dclaw/assets/turn_1_tactile.xml',
            'frame_skip':40,
            })
register(
    env_id='DClawTurnFixedT2-v0',
    class_path='robel.dclaw.turn_tactile:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN ,
    kwargs={'asset_path':'robel/dclaw/assets/turn_2_tactile.xml',
            'frame_skip':40,
            })
register(
    env_id='DClawTurnFixedT3-v0',
    class_path='robel.dclaw.turn_tactile:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN,
    kwargs={'asset_path':'robel/dclaw/assets/turn_3_tactile.xml',
            'frame_skip':40,
            })
register(
    env_id='DClawTurnFixedT4-v0',
    class_path='robel.dclaw.turn_tactile:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN,
    kwargs={'asset_path':'robel/dclaw/assets/turn_4_tactile.xml',
            'frame_skip':40,
            })
register(
    env_id='DClawTurnFixedT5-v0',
    class_path='robel.dclaw.turn_tactile:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN ,
    kwargs={'asset_path':'robel/dclaw/assets/turn_5_tactile.xml',
        'frame_skip':40,
        })
register(
    env_id='DClawTurnFixedT6-v0',
    class_path='robel.dclaw.turn_tactile:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN ,
    kwargs={'asset_path':'robel/dclaw/assets/turn_6_tactile.xml',
        'frame_skip':40,
        })

register(
    env_id='DClawTurnFixedT7-v0',
    class_path='robel.dclaw.turn_tactile:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN ,
    kwargs={'asset_path':'robel/dclaw/assets/turn_7_tactile.xml',
        'frame_skip':40,
        })

register(
    env_id='DClawTurnFixedT8-v0',
    class_path='robel.dclaw.turn_tactile:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN ,
    kwargs={'asset_path':'robel/dclaw/assets/turn_8_tactile.xml',
        'frame_skip':40,
        })

register(
    env_id='DClawTurnFixedT9-v0',
    class_path='robel.dclaw.turn_tactile:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN ,
    kwargs={'asset_path':'robel/dclaw/assets/turn_9_tactile.xml',
        'frame_skip':40,
        })
register(
    env_id='DClawTurnFixedT10-v0',
    class_path='robel.dclaw.turn_tactile:DClawTurnFixed',
    max_episode_steps=_TURN_EPISODE_LEN ,
    kwargs={'asset_path':'robel/dclaw/assets/turn_10_tactile.xml',
        'frame_skip':40,
        })





register(
    env_id='DClawTurnRandom-v0',
    class_path='robel.dclaw.turn:DClawTurnRandom',
    max_episode_steps=_TURN_EPISODE_LEN)

register(
    env_id='DClawTurnRandomDynamics-v0',
    class_path='robel.dclaw.turn:DClawTurnRandomDynamics',
    max_episode_steps=_TURN_EPISODE_LEN)


#===============================================================================
# Screw tasks
#===============================================================================

# Default number of steps per episode.
_SCREW_EPISODE_LEN = 80  # 80*40*2.5ms = 8s

register(
    env_id='DClawScrewFixed-v0',
    class_path='robel.dclaw.screw:DClawScrewFixed',
    max_episode_steps=_SCREW_EPISODE_LEN)

register(
    env_id='DClawScrewRandom-v0',
    class_path='robel.dclaw.screw:DClawScrewRandom',
    max_episode_steps=_SCREW_EPISODE_LEN)

register(
    env_id='DClawScrewRandomDynamics-v0',
    class_path='robel.dclaw.screw:DClawScrewRandomDynamics',
    max_episode_steps=_SCREW_EPISODE_LEN)
"""Grab Tasks"""
_GRAB_EPISODE_LEN = 160
register(
    env_id='DClawGrabFixedD0-v0',
    class_path='robel.dclaw.grab:DClawGrabFixed',
    max_episode_steps=_GRAB_EPISODE_LEN,
    kwargs={'asset_path':'robel/dclaw/assets/grab_0.xml',
            'frame_skip':4,
            })
register(
    env_id='DClawGrabFixedD1-v0',
    class_path='robel.dclaw.grab:DClawGrabFixed',
    max_episode_steps=_GRAB_EPISODE_LEN,
    kwargs={'asset_path':'robel/dclaw/assets/grab_1.xml',
            'frame_skip':4,
            })
register(
    env_id='DClawGrabFixedD2-v0',
    class_path='robel.dclaw.grab:DClawGrabFixed',
    max_episode_steps=_GRAB_EPISODE_LEN,
    kwargs={'asset_path':'robel/dclaw/assets/grab_2.xml',
            'frame_skip':4,
            })
register(
    env_id='DClawGrabFixedD3-v0',
    class_path='robel.dclaw.grab:DClawGrabFixed',
    max_episode_steps=_GRAB_EPISODE_LEN,
    kwargs={'asset_path':'robel/dclaw/assets/grab_3.xml',
            'frame_skip':4,
            })
register(
    env_id='DClawGrabFixedD4-v0',
    class_path='robel.dclaw.grab:DClawGrabFixed',
    max_episode_steps=_GRAB_EPISODE_LEN,
    kwargs={'asset_path':'robel/dclaw/assets/grab_4.xml',
            'frame_skip':4,
            })
# register(
#     env_id='DClawGrabFixedF0-v0',
#     class_path='robel.dclaw.grab_fixed:DClawGrabFixed',
#     max_episode_steps=_GRAB_EPISODE_LEN,
#     kwargs={'asset_path':'robel/dclaw/assets/fixed_grab_0.xml',
#             'frame_skip':4,
#             })
# register(
#     env_id='DClawGrabFixedF1-v0',
#     class_path='robel.dclaw.grab_fixed:DClawGrabFixed',
#     max_episode_steps=_GRAB_EPISODE_LEN,
#     kwargs={'asset_path':'robel/dclaw/assets/fixed_grab_1.xml',
#             'frame_skip':4,
#             })
# register(
#     env_id='DClawGrabFixedF2-v0',
#     class_path='robel.dclaw.grab_fixed:DClawGrabFixed',
#     max_episode_steps=_GRAB_EPISODE_LEN,
#     kwargs={'asset_path':'robel/dclaw/assets/fixed_grab_2.xml',
#             'frame_skip':4,
#             })
# register(
#     env_id='DClawGrabFixedF3-v0',
#     class_path='robel.dclaw.grab_fixed:DClawGrabFixed',
#     max_episode_steps=_GRAB_EPISODE_LEN,
#     kwargs={'asset_path':'robel/dclaw/assets/fixed_grab_3.xml',
#             'frame_skip':4,
#             })
# register(
#     env_id='DClawGrabFixedF4-v0',
#     class_path='robel.dclaw.grab_fixed:DClawGrabFixed',
#     max_episode_steps=_GRAB_EPISODE_LEN,
#     kwargs={'asset_path':'robel/dclaw/assets/fixed_grab_4.xml',
#             'frame_skip':4,
#             })

register(
    env_id='DClawGrabFixedF0-v0',
    class_path='robel.dclaw.grab_fixed:DClawGrabFixed',
    max_episode_steps=_GRAB_EPISODE_LEN / 2,
    kwargs={'asset_path':'robel/dclaw/assets/fixed_grab_0.xml',
            'frame_skip':20,
            })
register(
    env_id='DClawGrabFixedF1-v0',
    class_path='robel.dclaw.grab_fixed:DClawGrabFixed',
    max_episode_steps=_GRAB_EPISODE_LEN / 2,
    kwargs={'asset_path':'robel/dclaw/assets/fixed_grab_1.xml',
            'frame_skip':20,
            })
register(
    env_id='DClawGrabFixedF2-v0',
    class_path='robel.dclaw.grab_fixed:DClawGrabFixed',
    max_episode_steps=_GRAB_EPISODE_LEN / 2,
    kwargs={'asset_path':'robel/dclaw/assets/fixed_grab_2.xml',
            'frame_skip':20,
            })
register(
    env_id='DClawGrabFixedF3-v0',
    class_path='robel.dclaw.grab_fixed:DClawGrabFixed',
    max_episode_steps=_GRAB_EPISODE_LEN / 2,
    kwargs={'asset_path':'robel/dclaw/assets/fixed_grab_3.xml',
            'frame_skip':20,
            })
register(
    env_id='DClawGrabFixedF4-v0',
    class_path='robel.dclaw.grab_fixed:DClawGrabFixed',
    max_episode_steps=_GRAB_EPISODE_LEN / 2,
    kwargs={'asset_path':'robel/dclaw/assets/fixed_grab_4.xml',
            'frame_skip':20,
            })




register(
    env_id='DClawGrabFixedFF0-v0',
    class_path='robel.dclaw.grab_fixed_fixed_obj:DClawGrabFixed',
    max_episode_steps=_GRAB_EPISODE_LEN / 2,
    kwargs={'asset_path':'robel/dclaw/assets/fixed_grab_0_fixed_obj.xml',
            'frame_skip':20,
            })
register(
    env_id='DClawGrabFixedFF1-v0',
    class_path='robel.dclaw.grab_fixed_fixed_obj:DClawGrabFixed',
    max_episode_steps=_GRAB_EPISODE_LEN / 2,
    kwargs={'asset_path':'robel/dclaw/assets/fixed_grab_1_fixed_obj.xml',
            'frame_skip':20,
            })
register(
    env_id='DClawGrabFixedFF2-v0',
    class_path='robel.dclaw.grab_fixed_fixed_obj:DClawGrabFixed',
    max_episode_steps=_GRAB_EPISODE_LEN / 2,
    kwargs={'asset_path':'robel/dclaw/assets/fixed_grab_2_fixed_obj.xml',
            'frame_skip':20,
            })
register(
    env_id='DClawGrabFixedFF3-v0',
    class_path='robel.dclaw.grab_fixed_fixed_obj:DClawGrabFixed',
    max_episode_steps=_GRAB_EPISODE_LEN / 2,
    kwargs={'asset_path':'robel/dclaw/assets/fixed_grab_3_fixed_obj.xml',
            'frame_skip':20,
            })
register(
    env_id='DClawGrabFixedFF4-v0',
    class_path='robel.dclaw.grab_fixed_fixed_obj:DClawGrabFixed',
    max_episode_steps=_GRAB_EPISODE_LEN / 2,
    kwargs={'asset_path':'robel/dclaw/assets/fixed_grab_4_fixed_obj.xml',
            'frame_skip':20,
            })
"""insert environment"""
_GRAB_EPISODE_LEN = 800
register(
    env_id='DClawInsertFixedD0-v0',
    class_path='robel.dclaw.insert:DClawInsertFixed',
    max_episode_steps=_GRAB_EPISODE_LEN,
    kwargs={'asset_path':'robel/dclaw/assets/insert_0.xml',
            'frame_skip':4,
            })
register(
    env_id='DClawInsertFixedD1-v0',
    class_path='robel.dclaw.insert:DClawInsertFixed',
    max_episode_steps=_GRAB_EPISODE_LEN,
    kwargs={'asset_path':'robel/dclaw/assets/insert_1.xml',
            'frame_skip':4,
        })
register(
    env_id='DClawInsertFixedD2-v0',
    class_path='robel.dclaw.insert:DClawInsertFixed',
    max_episode_steps=_GRAB_EPISODE_LEN,
    kwargs={'asset_path':'robel/dclaw/assets/insert_2.xml',
            'frame_skip':4,
            })
register(
    env_id='DClawInsertFixedD3-v0',
    class_path='robel.dclaw.insert:DClawInsertFixed',
    max_episode_steps=_GRAB_EPISODE_LEN,
    kwargs={'asset_path':'robel/dclaw/assets/insert_3.xml',
            'frame_skip':4,
            })
register(
    env_id='DClawInsertFixedD4-v0',
    class_path='robel.dclaw.insert:DClawInsertFixed',
    max_episode_steps=_GRAB_EPISODE_LEN,
    kwargs={'asset_path':'robel/dclaw/assets/insert_4.xml',
            'frame_skip':4,
            })