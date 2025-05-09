import gymnasium as gym
import retro
import argparse
from stable_baselines3 import PPO
from stable_baselines3.common.atari_wrappers import ClipRewardEnv, WarpFrame
from torchinfo import summary
from stable_baselines3.common.vec_env import(
    SubprocVecEnv,
    VecFrameStack,
    VecTransposeImage,
)



'''
env = make_env()
obs = env.reset()
print(make_env())
venv = VecTransposeImage(VecFrameStack(SubprocVecEnv([make_env] * 3), n_stack=4))

model = PPO(
        policy="CnnPolicy",
        env=venv,
        learning_rate=lambda f: f * 2.5e-4,
        n_steps=128,
        batch_size=32,
        n_epochs=4,
        gamma=0.99,
        gae_lambda=0.95,
        clip_range=0.1,
        ent_coef=0.01,
        verbose=1,
    )
summary(model)
'''