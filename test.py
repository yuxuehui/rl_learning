
from utils import make_env,init_env
from stable_baselines3.common.vec_env import (
    DummyVecEnv,
    unwrap_vec_normalize,
)
init_env()
env = make_env('PandaPush-v3')
env = DummyVecEnv([env])
# info = env.unwrapped.sim.physics_client.getBodyInfo(object)
# print(info)

obs = env.reset()
done = False
while not done:
    action = env.action_space.sample() # random action
    obs, reward, done, info = env.step(action)
    object = env.envs[0].unwrapped.sim._bodies_idx['object']
    table = env.envs[0].unwrapped.sim._bodies_idx['table']
    print()
    # context 
    print(env.envs[0].unwrapped.sim.physics_client.getContactPoints(bodyA=table, bodyB=object, linkIndexA=-1,linkIndexB = -1))
    print()

# import datetime
# print(datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S-%f"))