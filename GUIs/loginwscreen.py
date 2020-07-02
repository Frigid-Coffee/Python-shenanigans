from tkinter import *

f=Tk()
f.title("Login")
f.geometry("150x150")

benutzer = {"Ben": "1234", "Tim":"Tim cool"}

def check():
    name = f.entry1.get()
    passwort = f.entry2.get()
    if name in benutzer:
        if passwort == benutzer[name]:
            f.label3.config(text = "Wilkommen benutzer")
            w = Tk()
            w.title("Welcome")
            f.geometry("150x150")
            if name == "Ben":
                w.label2 = Label(master = w, bg = "green", width = 20, height = 10)
                w.label1 = Label(master = w, bg = "green" , text = "Welcome "+ name + " You have just lost 1000 euros because you Tim stole them.")
            else:
                w.label2 = Label(master = w, bg = "yellow", width = 20, height = 10)
                w.label1 = Label(master = w, bg = "yellow" , text = "Welcome "+ name + " You have just won 1000 euros")
            w.label1.pack()
            w.label2.pack()
        else:
            f.label3.config(text = "Ihr Passwort ist falsch")
    else:
        f.label3.config(text = "Benutzer existiert nicht")
    
f.label = Label(master = f, text = "Anmeldung")
f.label1 = Label(master = f, text = "Benutzername:")
f.label2 = Label(master = f, text = "Passwort:")
f.label3 = Label(master = f, text = "")
f.entry1 = Entry(master = f)
f.entry2 = Entry(master = f)
f.button = Button(master = f, text = "login", command = check)







f.label.pack()
f.label1.pack()
f.entry1.pack()
f.label2.pack()
f.entry2.pack()
f.button.pack()
f.label3.pack()
f.mainloop()
