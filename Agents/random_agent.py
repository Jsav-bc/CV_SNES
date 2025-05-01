#Control agent to display progress of a psuedo random input agent
#Also easy implementation before attempting reward shaping for PPO agent

import retro

def make_env():
    env = retro.make(game='SuperMarioWorld-Snes',state='YoshiIsland2',scenario='SMW')
    return env

def main():
    env = make_env()
    obs = env.reset()
    while True:
        ob, totrew, terminated, truncated, info = env.step(env.action_space.sample())
        print(ob, totrew, terminated, truncated, info)
        env.render()
        if terminated:
            obs = env.reset()
    
    env.close()

if __name__ == "__main__":
    main()