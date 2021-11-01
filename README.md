# Reinforcement Lifelong Learning D'Claw Benchmark
## Overview
The benchmark includes 10 different manipulation tasks. The benchmark adapts from the D'Claw robot from [ROBEL](http://roboticsbenchmarks.org), a MuJoCo-based gym-compliant environment. The benchmarks consist of a robotic hand with three independent fingers. Each finger has three degrees of freedom. In our task, the robotic hand needs to turn the valve below 180 degrees.  The observation space of the benchmarks consists of joint angles, joint velocities, and the valve angle. The action space of the robot consists of robot joint angles. Each task only differs in the valve shape. All the tasks are designed to have dense rewards for a faster learning procedure. In our benchmark, each task is stable and easy to train. In our experiments, each policy can converge after 80,000 steps of updates using SAC.

## Getting started
### 1. Mujoco 
Download MuJoCo Pro 2.00 from the
[MuJoCo website](https://www.roboti.us/index.html). You should extract this
to `~/.mujoco/mujoco200`. Ensure your MuJoCo license key is placed at
`~/.mujoco/mjkey.txt`.

Add the following line to your `~/.bashrc` (or equivalent) in order for
`mujoco_py` to install properly:

```bash
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.mujoco/mujoco200/bin
```

Run `source ~/.bashrc` afterwards.
### 2. Benchmark
```bash
git clone https://github.com/fanyangcmu/RL_LL_DClaw_Benchmark.git
pip install -e RL_LL_DClaw_Benchmark/
```
### 3. Example Usage


```python
import robel
import gym

# Create a simulation environment for the D'Claw turn task.
env = gym.make('DClawTurnFixedT0-v0')

# Reset the environent and perform a random action.
env.reset()
env.step(env.action_space.sample())
```
### 4.Supported Environment
DClawTurnFixedT0-v0, DClawTurnFixedT1-v0, DClawTurnFixedT2-v0, DClawTurnFixedT3-v0, DClawTurnFixedT4-v0, DClawTurnFixedT5-v0, DClawTurnFixedT6-v0, DClawTurnFixedT7-v0, DClawTurnFixedT8-v0, DClawTurnFixedT9-v0, 

<!-- 
## Citation

```
@misc{ahn2019robel,
    title={ROBEL: Robotics Benchmarks for Learning with Low-Cost Robots},
    author={Michael Ahn and Henry Zhu and Kristian Hartikainen and Hugo Ponte and Abhishek Gupta and Sergey Levine and Vikash Kumar},
    year={2019},
    eprint={1909.11639},
    archivePrefix={arXiv},
    primaryClass={cs.RO}
}
``` -->
