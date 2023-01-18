import json
from tkinter import *

path = "C:\\Users\\apoll\\Desktop\\Dev\\NewAltis\\server-data\\resources\\[dev]\\Altis\\data"
file = open(path + "\\players.json")
file_dict = json.load(file)

window = Tk()
window.title("JSON Open App")
window.geometry("1090x600")
lb = Listbox()
frame = Frame()
frame.pack()
text = {}
for i in file_dict:
    lb.insert(lb.size()+1, i)

def lab(ind):
    for i in file_dict[ind]:
        text = Label(frame, text=i + " : " + str(file_dict[ind][i]))
        text.pack()

def loop():
    global frame
    frame.destroy()
    frame = Frame()
    frame.pack()
    if lb.curselection():
        lab(lb.get(lb.curselection()[0]))
    window.after(1000,loop)

lb.pack()
window.after(1000,loop)
window.mainloop()