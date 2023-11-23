import re
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import scrolledtext
from tkinter import filedialog as fd
from tkinter import messagebox
import ctypes as ct

def filename():
    filetypes = (
        ('text files', '*.txt'),
    )

    filename = fd.askopenfilename(filetypes=filetypes)
    file = open(filename, "r")
    for line in file:
        print(line)

    file.close()

root = tk.Tk()
root.title("TayLOL Sheesh-terpreter")
root.config(bg='#0c1818')
root.update()
set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
get_parent = ct.windll.user32.GetParent
set_window_attribute(get_parent(root.winfo_id()), 20, ct.byref(ct.c_int(2)), 4)

open = tk.Button(root, text='Open File', font=font.Font(size = 10), bd=1, command=lambda:filename(), bg='slateblue1', fg='white')
open.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")

open1 = Label(text = "LOL CODE Interpreter", font=font.Font(size = 12), fg='white',bg='#0c1818')
open1.grid(row=0, column=1, padx=5, pady=5, columnspan=2, sticky='W')

open2 = tk.Button(root, text='Open File', font=font.Font(size = 10), width = 17, bd=1, bg='white')
open2.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

text_area = scrolledtext.ScrolledText(root, wrap = tk.WORD, width = 33, height = 15, bg='#193433')
text_area.grid(row=1, column=0, padx=5, pady=5, rowspan=2, sticky="NSEW")

text_area1 = scrolledtext.ScrolledText(root, wrap = tk.WORD, width = 33, height = 15, bg='#193433')
text_area1.grid(row=2, column=1, padx=5, pady=5)

text_area2 = scrolledtext.ScrolledText(root, wrap = tk.WORD, width = 33, height = 15, bg='#193433')
text_area2.grid(row=2, column=2, padx=5, pady=5)

open3 = tk.Button(root, text='Open File', font=font.Font(size = 10), bd=1, bg='white')
open3.grid(row=3, column=0, padx=5, pady=5, columnspan=3, sticky="NSEW")

text_area4 = scrolledtext.ScrolledText(root, wrap = tk.WORD, height = 15, bg='#193433')
text_area4.grid(row=4, column=0, padx=5, pady=5, columnspan=3, sticky="NSEW")

root.mainloop()