Create Framestack Dataset,
    Create DB framework
        Label == Good, Bad, Neutral, Win
        Store frame data || f1.png ['file_path']
        Agg frame data into Frame stacks vid1_0001,"['f1.png','f2.png','f3.png','f4.png']",['Neutral']
    STRETCH GOAL
        Column Needed to seperate frames into respective runs and frame stacks can be genetaed from frames of the same run?
        Frame run counter for sequncing of frames?
        Utilize Skip frames 
        Recognize end states to reset game state
        captuer every frame then programatically generate frame stacks from base data


Convert Rl Reward mechanism to use classification values
    Good = 1
    Bad = -1
    Neutral = 0
    Win = 100

Feed RL frame data into db framework attempt auto lable and correct through manual labeling



Small crud app to create send frame stack and end user can manually label data
