from tkinter import *

window = Tk()
window.title("test")
window.geometry("1090x600")


frame = Frame()
frame.pack()

lb = Label(frame, text="BJ")
lb.pack()
lb = Label(frame, text="BJ")
lb.pack()
lb = Label(frame, text="BJ")
lb.pack()
lb = Label(frame, text="BJ")
lb.pack()

frame.destroy()

window.mainloop()