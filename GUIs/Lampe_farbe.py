from tkinter import *

x = 0

f=Tk()
f.title("Lampe")
f.geometry("150x150")

def schalten():
    if f.yellow == True:
        f.label.config(bg ="yellow", width = 10, height = 5)
        f.yellow = False
    else:
        f.label.config(bg ="black", width = 10, height = 5)
        f.yellow = True

f.label = Label(master = f, text = "")
f.button = Button(master = f, text = "Lampe schalten", command = schalten)

f.yellow = True
f.label.pack()
f.button.pack()
f.mainloop()
