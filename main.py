import json
import time
from tkinter import *

path = "C:\\Users\\apoll\\Desktop\\Dev\\NewAltis\\server-data\\resources\\[dev]\\Altis\\data"
file = open(path + "\\players.json", "r+")
file_dict = json.load(file)

window = Tk()
window.title("JSON Open App")
window.geometry("1090x900")

text = {}
name = ""
modifiedtable = {}

state = Label(text="State : Good")
state.pack()

lb = Listbox()
lb.pack()

frame = Frame()
frame.pack()

var = {}

def save():
    global frame
    if name != "":
        for i in frame.children:
            if "label" in i:
                id=frame.children[i].cget("text").replace(" : ", "")
                modifiedtable[id] = var[id].get()
        file_dict[name] = modifiedtable
        #print(json.dumps(file_dict))
        open(path + "\\players.json", "w+").write(json.dumps(file_dict))

btn = Button(text="Save", command=save)
btn.pack()

for i in file_dict:
    lb.insert(lb.size()+1, i)

def lab(ind):
    global name
    global frame
    if name != ind:
        frame.destroy()
        frame = Frame()
        frame.pack()
        for i in file_dict[ind]:
            text = Label(frame, text=i + " : ")
            text.pack()
            var[i] = StringVar()
            input_ = Entry(frame, textvariable=var[i])
            input_.pack()
            input_.insert(0, file_dict[ind][i])
        name = ind

def loop():
    if lb.curselection():
        lab(lb.get(lb.curselection()[0]))
    window.after(1000,loop)

window.after(10,loop)
window.mainloop()