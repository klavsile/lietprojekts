import os

import tkinter as tk
from tkinter import font
from tkinter import filedialog as fd

import ffmpeg

root = tk.Tk()
root.title('Projekts')
root.resizable(False, False)
root.geometry('300x400')
colors = {"window": "#2e2633", "button": "#99173c", "text": "#2e2633", "text2": "#99173c", "entry": "#99173c"}
root.configure(bg=colors["window"])

videoDir = ""

#Atver attēla izvēles logu
def OpenFile(output):
    filetypes = (
        ("Video files", "*.mp4;*.mov;*.gif"),
    )

    videoDir = fd.askopenfilename(
        title='Select File',
        initialdir=os.path.dirname(os.path.realpath(__file__)),
        filetypes=filetypes)
    ConvertFile(videoDir, output)

def ConvertFile(dir, output):
            
    dir_path = os.path.dirname(os.path.realpath(__file__))
    (
        ffmpeg.input(dir)
        .output(dir_path + "/output" + output)
        .run()
    )

roboto12 = font.Font(family='Roboto', size=12, weight='bold')

Label = tk.Label(
    root,
    text='Convert .gif .mp4 .mov files\nand upload them to file.io',
    font=roboto12,
    bg=colors["window"],
    fg=colors["text2"],
)
Label.place(x=30, y=20)

Entry1 = tk.Entry(
    root,
    text='width',
    font=roboto12,
    width=5,
    bg=colors["entry"],
    fg=colors["text"],
)
Entry1.place(x=60, y=80)

Entry1Text = tk.Label(
    root,
    text='Width',
    font=roboto12,
    bg=colors["window"],
    fg=colors["text2"],
)
Entry1Text.place(x=10, y=80)

Entry2 = tk.Entry(
    root,
    text='height',
    font=roboto12,
    width=5,
    bg=colors["entry"],
    fg=colors["text"],
)
Entry2.place(x=220, y=80)

Entry2Text = tk.Label(
    root,
    text='Height',
    font=roboto12,
    bg=colors["window"],
    fg=colors["text2"],
)
Entry2Text.place(x=160, y=80)

ConvertToGif = tk.Button(
    root,
    text='Convert file to .gif',
    height=2,
    width=16,
    font=roboto12,
    bg=colors["button"],
    fg=colors["text"],
    command=lambda: OpenFile(".gif")
)
ConvertToGif.place(x=80, y=100)

ConvertToMp4 = tk.Button(
    root,
    text='Convert file to .mp4',
    height=2,
    width=16,
    font=roboto12,
    bg=colors["button"],
    fg=colors["text"],
    command=lambda: OpenFile(".mp4")
)
ConvertToMp4.place(x=80, y=180)

ConvertToMov = tk.Button(
    root,
    text='Convert file to .mov',
    height=2,
    width=16,
    font=roboto12,
    bg=colors["button"],
    fg=colors["text"],
    command=lambda: OpenFile(".mov")
)
ConvertToMov.place(x=80, y=260)

root.mainloop()