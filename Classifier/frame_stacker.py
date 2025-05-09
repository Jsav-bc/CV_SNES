import os


def framestacker(folder_path,skip_frame = 3,frame_stack_len = 3):
    folder_path = folder_path
    skip_frame = skip_frame
    frame_stack_len = frame_stack_len
    p_fold = folder_path.split('/')[-1]
    ifiles = []

    for f in os.listdir(folder_path):
        i_file = {
        "fpath": (f"{folder_path}/{f}"),
        "sequ": int(f.rsplit('/')[-1].split('_')[0])
        }
        ifiles.append(i_file)
    image_files = sorted(ifiles,key=lambda x: x['sequ'])

    framestacks_ls = []
    framestacks = []

    for i in image_files:
        f_stack = []
        base_index = i['sequ']
        m = len(image_files)
        for j in range(frame_stack_len):
            frame_index = base_index + j*skip_frame
            if frame_index >= m :
                f_stack.append(m-1)
            else:
                f_stack.append(frame_index)
        framestacks.append(f_stack)
        

    for framestack in framestacks:
        framestacks_lib = {
        'event': p_fold,
        'run_id': framestack,
        'frame_seq': [image_files[i]['fpath'] for i in framestack],
        'label': None,
        'Train': False,
        'Verified': False
        }
        framestacks_ls.append(framestacks_lib)
    
    return framestacks_ls