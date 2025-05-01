import retro
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import(
    SubprocVecEnv,
    VecFrameStack,
    VecTransposeImage,
)
from Wrappers import NoProgressPenaltyWrapper

def make_env():
    def _init():
        env = retro.make(game='SuperMarioWorld-Snes',state='YoshiIsland2',scenario='SMW')
        env = NoProgressPenaltyWrapper(env,timeout=2000)
        return env
    return _init
def main():
    venv = VecTransposeImage(VecFrameStack(SubprocVecEnv([make_env()] * 6), n_stack=4))

    model = PPO(
            policy="CnnPolicy",
            env=venv,
            learning_rate=lambda f: f * 2.5e-3,
            n_steps=256,
            batch_size=32,
            n_epochs=4,
            gamma=0.99,
            gae_lambda=0.95,
            clip_range=0.1,
            ent_coef=0.01,
            verbose=1,
        )

    model.learn(total_timesteps = 100000)
    model.save("ppo_smb")

    obs = venv.reset()

if __name__ == "__main__":
    main()
'''
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = venv.step(action)
    print(obs,rewards,dones,info)
    venv.render()
'''