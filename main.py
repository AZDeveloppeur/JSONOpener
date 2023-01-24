from tkinter.filedialog import askopenfilename
filename = askopenfilename()

import json
import config
from window import window
from tkinter import *

if not filename:
    exit()

file = open(filename, "r+")
file_dict = json.load(file)

text = {}
name = ""
modifiedtable = {}
already_registered = False

state = Label(text="State : Good", bg=config.background, foreground=config.foreground)
state.pack()

lb = Listbox(bg=config.background, foreground=config.foreground)
lb.pack()

frame = Frame(bg=config.background)
frame.pack()

var = {}

def save():
    global frame
    global modifiedtable
    modifiedtable = {}
    if name != "":
        for i in frame.children:
            if "label" in i:
                id=frame.children[i].cget("text").replace(" : ", "")
                modifiedtable[id] = var[id].get()
        file_dict[name] = modifiedtable
        open(filename, "w+").write(json.dumps(file_dict))

btn = Button(text="Save", command=save, bg=config.background, foreground=config.foreground)
btn.pack()

def lab(ind):
    global name
    global frame
    if ind != "main":
        if name != ind:
            frame.destroy()
            frame = Frame(bg=config.background)
            frame.pack()
            for i in file_dict[ind]:
                text = Label(frame, text=i + " : ", bg=config.background, foreground=config.foreground)
                text.pack()
                var[i] = StringVar()
                input_ = Entry(frame, textvariable=var[i], width=100)
                input_.pack()
                input_.insert(0, file_dict[ind][i])
            name = ind
    else:
        if name != ind:
            frame.destroy()
            frame = Frame(bg=config.background)
            frame.pack()
            for i in file_dict:
                if not "dict" in str(type(file_dict[i])):
                    text = Label(frame, text=i + " : ", bg=config.background, foreground=config.foreground)
                    text.pack()
                    var[i] = StringVar()
                    input_ = Entry(frame, textvariable=var[i], width=100)
                    input_.pack()
                    input_.insert(0, file_dict[i])
            name = ind

for i in file_dict:
    if "dict" in str(type(file_dict[i])):
        lb.insert(lb.size()+1, i)
    else:
        if not already_registered:
            lb.insert(lb.size()+1, "main")
            already_registered = True
        lab("main")

def loop():
    if lb.curselection():
        lab(lb.get(lb.curselection()[0]))
    window.after(1000,loop)

window.after(10,loop)
window.mainloop()