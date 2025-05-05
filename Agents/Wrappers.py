from gymnasium import Wrapper
import numpy as np

class NoProgressPenaltyWrapper(Wrapper):
    def __init__(self,env,timeout=0):
        super().__init__(env)
        self.timeout = timeout
        self.penelty = 0
        self.steps_past_reward = 0

    def reset(self, **kwargs):
        self.steps_past_reward = 0
        return self.env.reset(**kwargs)
    
    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)

        if reward <= 0:
            self.steps_past_reward += 1
        else:
            self.steps_past_reward = 0

        if self.steps_past_reward > self.timeout:
            penalty = ((self.steps_past_reward - self.timeout) * 0.0001)
            reward += np.float32(-1*(penalty))
            info["no_progress_penalty"] = True
        else:
            info["no_progress_penalty"] = False

        return obs, reward, terminated, truncated, info
    
class OneUpWrapper(Wrapper):
    def __init__(self,env):
        super().__init__(env)
        self.reward = 0
        self.steps_past_reward = 0
    
    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)


        return obs, reward, terminated, truncated, info