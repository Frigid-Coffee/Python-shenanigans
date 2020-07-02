#GUI

from tkinter import *

def greet():
    f.label.config(text = "Greetings")

def bye():
    f.label2.config(text = "Bye")

f=Tk()
f.title("Hello World")
f.geometry("500x500")


f.label = Label(master = f, text = "Hello")
f.label.pack()

f.button = Button(master = f, text = "Press me", command = greet)
f.button.pack()

f.label2 = Label(master = f, text = "Bid Farewell")
f.label2.pack()

f.button2 = Button(master = f, text = "Press me", command = bye)
f.button2.pack()


f.mainloop()
