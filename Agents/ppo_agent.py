import retro
import imageio
import numpy as np
import os
import imageio
import random
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import(
    SubprocVecEnv,
    VecFrameStack,
    VecTransposeImage,
)
from Wrappers import NoProgressPenaltyWrapper

def make_env():
    def _init():
        #env = retro.make(game='SuperMarioWorld-Snes',state='YoshiIsland2',scenario='SMW')
        env = retro.make(game='Airstriker-Genesis',render_mode='rgb_array')
        #env = NoProgressPenaltyWrapper(env,timeout=2500)
        return env
    return _init
def main():
    #TODO Receive Parent ID from DB 
    venv = VecTransposeImage(VecFrameStack(SubprocVecEnv([make_env()] * 1), n_stack=4))

    model = PPO(
            policy="CnnPolicy",
            env=venv,
            learning_rate=lambda f: f * 2.5e-3,
            n_steps=128,
            batch_size=32,
            n_epochs=2,
            gamma=0.99,
            gae_lambda=0.95,
            clip_range=0.1,
            ent_coef=0.01,
            verbose=1,
        )

    model.learn(total_timesteps = 1280)
    model.save("ppo_as")

    images = []
    obs = venv.reset()
    img = model.env.render(mode="rgb_array")
    event_id = random.random()
    os.mkdir(f"/home/jordan/boot/snesai/CV_SNES/Games_States/{event_id}")
    
    for i in range(350):
        images.append(img)
        action,_ = model.predict(obs)
        obs,_,_,_ = model.env.step(action)
        img = model.env.render(mode="rgb_array")
        imageio.imwrite(f"/home/jordan/boot/snesai/CV_SNES/Games_States/{event_id}/{i}_test.png",img)

if __name__ == "__main__":
    main()