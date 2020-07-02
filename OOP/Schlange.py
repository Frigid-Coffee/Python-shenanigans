from random import random

class Schlange(object):
    def __init__(self):
        self.liste = []

    def istLeer(self):
        if self.liste == []:
            return True
        else:
            return False

    def mitLetztem(self, element):
        self.liste = self.liste + [element]

    def ohneErstes(self):
        if not self.istLeer():
            self.liste = self.liste[1:]

    def erstes(self):
        if self.istLeer():
            return None
        else:
            return self.liste[0]
        
    def anzahlElemente(self):
        return len(self.liste)

    def getSchlange(self):
        return self.liste

    def setSchlange(self, liste):
        self.liste = liste

s = Schlange()

#jede 1 stellt ein Mensch in der Schlange dar
s.setSchlange([1, 1, 1, 1])
wAnstellen = 0.6
wBedienen = 0.65
while s.istLeer() == False:
    print(s.getSchlange())
    if random() <= wAnstellen:
        s.mitLetztem(1)
    if random() <= wBedienen:
        s.ohneErstes()
print("Die Schlange ist leer")
