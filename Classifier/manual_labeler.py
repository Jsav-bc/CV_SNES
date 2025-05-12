from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("Animated GIF Viewer")

image_path = r"Games_States_Gifs\0.5698117157520127\250_test.gif"

pil_gif = Image.open(image_path)

frames = []
try:
    while True:
        frame = pil_gif.copy()
        frames.append(ImageTk.PhotoImage(frame))
        pil_gif.seek(len(frames))  # go to next frame
except EOFError:
    pass  # No more frames

frame_count = len(frames)
frm = ttk.Frame(root, padding=10)
frm.grid()

label = Label(frm)
label.grid(column=0, row=0, columnspan=4)

label.frames = frames

# Animation loop
def update(idx):
    label.configure(image=frames[idx])
    root.after(100, update, (idx + 1) % frame_count)

update(0)

# Buttons
ttk.Button(frm, text="Good").grid(column=0, row=1)
ttk.Button(frm, text="Bad").grid(column=1, row=1)
ttk.Button(frm, text="Neutral").grid(column=2, row=1)
ttk.Button(frm, text="Win").grid(column=3, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2, columnspan=4)

root.mainloop()
