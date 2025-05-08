import os
import imageio
import torch
import torchvision
import torchvision.transforms
import cv2 

folder_path = "/home/jordan/boot/snesai/CV_SNES/Games_States/0.5222159894470562"
frame_stack_len = 4

image_files = sorted([os.path.join(folder_path, f) for f in os.listdir(folder_path)])

framstacks = []

for i in image_files:
    f_stack = []
    for j in range(frame_stack_len):
        f_stack.append(image_files[j])
    framstacks.append(f_stack)
    j+=1

print(framstacks)