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

