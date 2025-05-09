import os
import imageio
import torch
import torchvision
import torchvision.transforms
import cv2 

folder_path = "/home/jordan/boot/snesai/CV_SNES/Games_States/0.5222159894470562"
frame_stack_len = 6

ifiles = []

for f in os.listdir(folder_path):
    i_file = {
    "fpath": (f"{folder_path}/{f}"),
    "sequ": int(f.rsplit('/')[-1].split('_')[0])
    }
    ifiles.append(i_file)
image_files = sorted(ifiles,key=lambda x: x['sequ'])

framestacks_lib = {
    'run_id': '',
    'frame_seq': []
}
framestacks = []

for i in image_files:
    f_stack = []
    base_index = i['sequ']
    m = len(image_files)
    for j in range(frame_stack_len):
        frame_index = base_index + j*3
        if frame_index >= m :
            f_stack.append(m-1)
        else:
            f_stack.append(frame_index)
    framestacks.append(f_stack)
    

print(framestacks)