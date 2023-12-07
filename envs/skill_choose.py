from collections import defaultdict
from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
from stable_baselines3.common.vec_env import DummyVecEnv
import copy
import random
from utils import *

class TestEnv(Env):
    def __init__(self,
                 name, 
                 lateral_friction, 
                 spinning_friction,
                 mass, 
                 gravity, 
                 object_height,
                 time_steps,
                 reward_type='Dense',
                 agent_type='default',
                 info_phase_length=10,
                 action_range=[0, 1]
                 ):
        """
        Create a stable_baselines-compatible environment to train policies on
        :param agent_type: 'default'；不可修改
        :param info_phase_length: episode的最大步长，注意不同阶段最大步长不同；在create函数中作为超参转入；
        :param vertex: action干预的node的编号
        :param list_last_vertex: List格式，其中元素为Dict格式；
                            前序阶段的agent信息，用来生成本阶段的goal；
                            若为x3-x12阶段（即没有前序阶段），则为空[];
                            反序的！例：x10-x5(当前阶段),x5-x3,x3-x12;
                            生成goal的时候是从后往前遍历，逐阶段生成goal;
        :param train:
        """
        # vg = 1.886280201
        self.logger = None
        self.log_data = defaultdict(int)
        self.agent_type = agent_type
        self.ep_rew = 0
        self.reward_env = []  # 生成env列表
        self.reward_goal = []  # 生成goal列表
        self.reward_state = []  # 记录各个阶段 当前时刻 状态信息

        self.action_space = Box(action_range[0], action_range[1], (2,), dtype=np.float32)
        self.observation_space = Box(0, np.inf, (6,))
        self.info_phase_length = info_phase_length

        # 用来生成obs
        if name == "PandaPush-v3":
            print("This is PandaPush-v3 Env, Welcome!")
            self.env_sim = DummyVecEnv([get_push_env(lateral_friction=lateral_friction, mass=mass,train_time_steps=time_steps)])
            # print("******************", self.env_sim)
        elif name == "PandaPickAndPlace-v3":
            print("This is PandaPickAndPlace-v3 Env, Welcome!")
            self.env_sim = DummyVecEnv([get_pick_and_place_env(lateral_friction=lateral_friction, mass=mass, train_time_steps=time_steps)])
        else:
            raise Exception("Unkown Environment in make_env")

        self.balance_flag = 0
        self.friction_push_range = [0.1, 1.0]
        self.friction_pick_range = [1.0, 10.0]
        self.mass_pick_range = [0.5, 6.0]
        self.mass_push_range = [6.0, 15.0]

    def step(self, action):
        """
            state: obs + causal factors
            action: skill的选择,0/1? policy的输出是1维度的还是2维度的需要考虑一下
            return: 
        """
        info = dict()
        action = action/(np.sum(action)+1e-8)
        if action[0]>=action[1]:
            action=[1,0]
        else:
            action=[0,1]

        
        next_state=copy.deepcopy(self.state)
        if self.state[0] > self.friction_push_range[1]:
            if self.state[1] > self.mass_pick_range[1]:
                # continue
                if action[0] == 1: # Push
                    reward = -10
                    done=False
                else:              # Pick
                    reward = -10
                    done=False
            else:
                if action[0] == 1: # Push
                    reward = -10
                    done=False
                else:              # Pick, small mass & big friction
                    reward = 10
                    for i in range(2, 6):
                        next_state[i] = 0
                    next_state[3] = 1
        else:
            if self.state[1] > self.mass_pick_range[1]:
                if action[0] == 1: # Push, big mass & small friction
                    reward = 10
                    for i in range(2, 6):
                        next_state[i] = 0
                    next_state[4] = 1
                    done=True
                else:             # Pick
                    reward = -10
                    done=False
            else:
                if action[0] == 1: # Push, small mass & small friction
                    reward = 10
                    for i in range(2, 6):
                        next_state[i] = 0
                    next_state[4] = 1
                    done=True
                else:
                    reward = 10     # Pick, small mass & samll friction
                    for i in range(2, 6):
                        next_state[i] = 0
                    next_state[3] = 1
                    done=True
        self.info_steps+=1
        if self.info_steps == self.info_phase_length-1 or done is True:  # 最后一步
            self.ep_rew = self.ep_rew + reward  # 计算累计奖励
            info["episode"] = dict()
            info["episode"]["r"] = self.ep_rew  # episode的reward
            info["episode"]["l"] = self.info_steps  # episode的长度

            done = True
            self.ep_rew = 0.0
        else:
            self.ep_rew = self.ep_rew + reward  # 计算累计奖励

        self.state=copy.deepcopy(next_state)
        return self.state, reward, done, info

    def log_callback(self):
        for k, v in self.log_data.items():
            self.logger.logkv(k, v)
        self.log_data = defaultdict(int)

    def reset(self):
        import random

        # 具体obs采样，是action之后重新采样？还是一个episode就用一个obs？
        self.obs = self.env_sim.reset()
        
        # 暂时设定为随机采样，之后需要均衡样本
        friction = random.random(self.friction_push_range[0],self.friction_pick_range[1])
        mass = random.random(self.mass_pick_range[0],self.mass_push_range[1])

        self.state=np.array([friction,mass,self.obs])
        self.info_steps=0
        # print("reset")
        # print(now_insulin)
        return self.state

    def render(self, mode='human'):
        pass

    def close(self):
        pass

    def seed(self, seed=94566):
        np.random.seed(seed)