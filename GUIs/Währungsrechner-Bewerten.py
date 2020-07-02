from  tkinter import *

f = Tk()
f.title("Währungsrechner")
f.geometry("350x250")

currency = StringVar()

def convert():
    euro = float(e.get())
    if currency.get() == "gb":
        umrech = euro * 0.9
    else:
        umrech = euro * 1.1
    l2.config(text = str(umrech))

l = Label(f, text = "Geben Sie einen Betrag in Euro ein und wählen Sie eine Währung")
l2 = Label(f)
e = Entry(f)
r = Radiobutton(f, text = "GB£", value = "gb", variable = currency)
r2 = Radiobutton(f, text = "US$", value = "us", variable = currency)

b = Button(f,text = "umrechnung" , command= convert)

l.pack()
e.pack()
r.pack()
r2.pack()
b.pack()
l2.pack()
f.mainloop()
