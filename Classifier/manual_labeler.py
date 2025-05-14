from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

#set class so that eaiser to label frame dicts at runtime
#TODO image path as varible and add func to buttons to label stacks

class gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("Manual Labeler")

        image_path = r"Games_States_Gifs\0.5698117157520127\250_test.gif"

        pil_gif = Image.open(image_path)

        gframes = []
        try:
            while True:
                gframe = pil_gif.copy()
                gframes.append(ImageTk.PhotoImage(gframe))
                pil_gif.seek(len(gframes))
        except EOFError:
            pass

        frame = ttk.Frame(self, padding=10)
        frame.grid()
        
        label = Label(frame)
        label.grid()

        label.gframes = gframes
        
        frame_count = len(gframes)
        def update(idx):
            label.configure(image=gframes[idx])
            next_idx = (idx + 1)% frame_count
            self.after(100, update, next_idx)

        update(0)

        # Buttons
        ttk.Button(frame, text="Good",).grid(column=0, row=1)
        ttk.Button(frame, text="Bad").grid(column=1, row=1)
        ttk.Button(frame, text="Neutral").grid(column=2, row=1)
        ttk.Button(frame, text="Win").grid(column=3, row=1)
        ttk.Button(frame, text="Quit", command=self.destroy).grid(column=0, row=2, columnspan=4)

app = gui()
app.mainloop()
