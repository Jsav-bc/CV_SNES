import frame_stacker
import imageio
import os

ls = frame_stacker.framestacker("/home/jordan/boot/snesai/CV_SNES/Games_States/0.5698117157520127", skip_frame=3,frame_stack_len=4)

run = 0
for framestack in ls:
    run += 1
    try:
        os.mkdir(f"/home/jordan/boot/snesai/CV_SNES/Games_States_Gifs/{framestack['event']}")
    except:
        pass
    f_image = []
    for i in framestack['frame_seq']:
        f_image.append(imageio.v3.imread(i))
    imageio.mimsave(f"/home/jordan/boot/snesai/CV_SNES/Games_States_Gifs/{framestack['event']}/{run}_test.gif",f_image)