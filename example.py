import robel
import gym

# Create a simulation environment for the D'Claw turn task.
env = gym.make('DClawTurnFixedT2-v0')

done = False
obs = env.reset()

while not done:
    print(obs)
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    # env.render()

