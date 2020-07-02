
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def verschieben(self, x, y):
        self.x += x
        self.y += y
    def getKoordinaten(self):
        return([self.x, self.y])
    def __str__(self):
        return str(self.x) + "|" + str(self.y)
        
class Neck:
    def __init__(self, punkte):
        self.punkte = punkte
        self.Koordinaten = []
    def verschieben(self, x, y):
        for n in range(len(self.punkte)):
            self.punkte[n].verschieben(x, y)
    def __str__(self):
        for n in range(len(self.punkte)):
            self.Koordinaten.append(str(self.punkte[n].x) + "|" + str(self.punkte[n].y))
        return str(self.Koordinaten)

class Figur:
    def __init__(self):
        self.Neck = []
    def hinzufuegen(self, Neck):
        self.Neck.append(Neck)
    def verschieben(self, x, y):
        for n in range(len(self.Neck)):
            self.Neck[n].verschieben(x, y)
    def getKoordinaten(self):
        self.Koordinaten = []
        for n in range(len(self.Neck)):
            self.Koordinaten.append("Koordinaten des Necks: ")
            for m in range(len(self.Neck[n].punkte)):
                self.Koordinaten.append(str(self.Neck[n].punkte[m].x) + "|" + str(self.Neck[n].punkte[m].y))
        return str(self.Koordinaten)
    def __str__(self):
        return "Koordinaten der Figur: " + self.getKoordinaten()




# Punkte
p1 = Punkt(0, 0)
p2 = Punkt(0, 10)
p3 = Punkt(10, 10)
p4 = Punkt(10, 0)
p5 = Punkt(0, 10)
p6 = Punkt(10, 10) 
p7 = Punkt(5, 15)
print("Koordinaten der Punkte: ", end = "")
print(p1, p2, p3, p4, p5, p6, p7)
# Rechtecke und Dreieck (als n-Eck)
rechteck = Neck([p1, p2, p3, p4])
dreieck = Neck([p5, p6, p7])
print("Koordinaten des Rechtecks: ", rechteck)
# Haus des Nikolaus als Figur
haus_nikolaus = Figur()
haus_nikolaus.hinzufuegen(rechteck)
print(haus_nikolaus)
haus_nikolaus.hinzufuegen(dreieck)
print(haus_nikolaus)
# Figur verschieben
haus_nikolaus.verschieben(2, 3)
print("Neue", haus_nikolaus)
 
