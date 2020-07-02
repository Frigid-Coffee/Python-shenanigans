from tkinter import *

f=Tk()
f.title("Lampe")
f.geometry("500x500")

def anschalten():
    f.label.config(text = "Lampe an")
def ausschalten():
    f.label.config(text = "Lampe aus")
    
f.label = Label(master = f, text = "")

f.button1 = Button(master = f, text = "Lampe anschalten", command = anschalten)
f.button2 = Button(master = f, text = "Lampe ausschalten", command = ausschalten)

f.label.pack()
f.button1.pack()
f.button2.pack()
f.mainloop()
