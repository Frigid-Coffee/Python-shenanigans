from tkinter import *
import random as r

f = Tk()
f.title("Zahlenraten")
f.geometry("500x500")

f.num = str(r.randint(0,10))
f.versuche = 5

def restart():
    f.versuche = 5
    f.num = str(r.randint(0,10))
    l.config(text = "Raten sie eine zahl zwischen 1 und 10")
    l1.config(text = "versuche: " + str(f.versuche))
    l2.config(text = "")
    l3.config(text = "")
    b.config(text = "Tipp abgeben", command = checknum, state = NORMAL)
    e.config(state = NORMAL)

def checknum():
    guess = e.get()
    glist = ""
    glist += guess
    if guess == f.num:
        l2.config(text = "Richtig")
        l3.config(text = "Gewonnen!")
        b.config(state = DISABLED)
        e.config(state = DISABLED)
    else:
        l2.config(text = "Falsch")
        f.versuche -= 1
        l1.config(text = "versuche: " + str(f.versuche))
        if f.versuche == 0:
            l3.config(text = "Verloren")
            b.config(state = DISABLED)
            e.config(state = DISABLED)

l = Label(f, text = "Raten sie eine zahl zwischen 1 und 10")
l3 = Label(f, text = "")
b2 = Button(f, text = "Neustart", command = restart)

rahmen = Frame(f, relief = RIDGE, bd = 2)
l1 = Label(rahmen, text = "versuche: " + str(f.versuche))
l2 = Label(rahmen, text = "")
e = Entry(rahmen)
b = Button(rahmen, text = "Tipp abgeben", command = checknum)


l3.pack()
l.pack()

rahmen.pack()
l1.pack()
e.pack()
b.pack()
l2.pack()

b2.pack()

f.mainloop()
