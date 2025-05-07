#Control agent to display progress of a psuedo random input agent
#Also easy implementation before attempting reward shaping for PPO agent

import retro
import imageio
import random
import os

def make_env():
    #env = retro.make(game='SuperMarioWorld-Snes',state='YoshiIsland2',scenario='SMW')
    env = retro.make(game='Airstriker-Genesis',render_mode='rgb_array')
    return env

def main():
    env = make_env()
    obs = env.reset()
    event_id = random.random()
    os.mkdir(f"{event_id}")
    i = 0
    while True:
        i+=1
        ob, totrew, terminated, truncated, info = env.step(env.action_space.sample())
        print(ob, totrew, terminated, truncated, info)
        img = env.render()
        imageio.imwrite(f"{event_id}/{i}_test.png",img)
        if terminated:
            i = 0
            event_id = random.random()
            os.mkdir(f"{event_id}")
            obs = env.reset()
    
    env.close()

if __name__ == "__main__":
    main()