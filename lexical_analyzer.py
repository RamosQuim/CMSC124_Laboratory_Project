import re
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import scrolledtext
from tkinter import filedialog as fd
import ctypes as ct

def filename():
    filetypes = (
        ('text files', '*.txt'),
    )

    filename = fd.askopenfilename(filetypes=filetypes)
    file = open(filename, "r")
    textEditor.delete("1.0", "end")
    textEditor.insert("end", file.read(), ("centered",))
    
    file.close()

root = tk.Tk()
root.title("TayLOL Sheesh-terpreter")
root.config(bg='#0c1818')
root.resizable(False, False)
root.update()
set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
get_parent = ct.windll.user32.GetParent
set_window_attribute(get_parent(root.winfo_id()), 20, ct.byref(ct.c_int(2)), 4)

openButton = tk.Button(root, text='Open File', font=font.Font(size = 10), bd=1, bg='#365963', fg='white', command=lambda:filename())
openButton.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")

title = Label(text = "LOL CODE Interpreter", font=font.Font(size = 12, weight='bold'), fg='white',bg='#0c1818')
title.grid(row=0, column=1, padx=5, pady=5, columnspan=2, sticky='W')

lexemeHeader = Label(text = "Lexemes", font=font.Font(size = 12), fg='white', bg='#0c1818', borderwidth=1, relief="ridge")
lexemeHeader.grid(row=1, column=1, padx=5, sticky='NSEW')

symbolHeader = Label(text = "Symbol Table", font=font.Font(size = 12), fg='white', bg='#0c1818', borderwidth=1, relief="ridge")
symbolHeader.grid(row=1, column=2, padx=5, sticky='NSEW')

textEditor = scrolledtext.ScrolledText(root, width = 33, height = 15, bg='#193433', fg='white')
textEditor.grid(row=1, column=0, padx=5, pady=5, rowspan=2, sticky="NSEW")

lexemes = ttk.Treeview(root, selectmode='browse', height=15)
lexemes.grid(row=2, column=1, padx=5, pady=5)
lexemes['columns'] = ('lexeme', 'classification')
lexemes.column("#0", width=0,  stretch=NO)
lexemes.column("lexeme",anchor=CENTER, width=165,stretch=NO)
lexemes.column("classification",anchor=CENTER, width=165,stretch=NO)
lexemes.heading("#0",text="",anchor=CENTER)
lexemes.heading("lexeme",text="Lexeme",anchor=CENTER)
lexemes.heading("classification",text="Classification",anchor=CENTER)

symbolTable = ttk.Treeview(root, selectmode='browse', height=15)
symbolTable.grid(row=2, column=2, padx=5, pady=5)
symbolTable['columns'] = ('identifier', 'value')
symbolTable.column("#0", width=0,  stretch=NO)
symbolTable.column("identifier",anchor=CENTER, width=165,stretch=NO)
symbolTable.column("value",anchor=CENTER, width=165,stretch=NO)
symbolTable.heading("#0",text="",anchor=CENTER)
symbolTable.heading("identifier",text="Identifier",anchor=CENTER)
symbolTable.heading("value",text="Value",anchor=CENTER)

executeButton = tk.Button(root, text='EXECUTE', font=font.Font(size = 10), bd=1, bg='#365963', fg='white')
executeButton.grid(row=3, column=0, padx=5, pady=5, columnspan=3, sticky="NSEW")

text_area4 = scrolledtext.ScrolledText(root, wrap = tk.WORD, height = 15, fg='white', bg='#193433')
text_area4.grid(row=4, column=0, padx=5, pady=5, columnspan=3, sticky="NSEW")

# style of tables
style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview.Heading", background="#365963", foreground="white", relief="flat")
style.configure("Treeview", background="#193433", fieldbackground="#193433", foreground="white")

root.mainloop()