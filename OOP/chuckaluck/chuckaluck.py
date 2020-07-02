import random as r

class Konto:
    def __init__(self, stand):
        self.stand = stand

    def einzahlen(self, betrag):
        self.stand += betrag

    def auszahlen(self, betrag):
        self.stand -= betrag

class Spielzahl:
    def __init__(self, zahl):
        self.zahl = zahl

    def setzen(self, wert):
        self.zahl = wert

class Wuerfel:
    def __init__(self):
        self.augen = r.randint(1,6)

    def werfen(self):
        self.augen = r.randint(1,6)




