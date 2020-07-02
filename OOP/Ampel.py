

class Ampel():
    def __init__(self):
        self.g = False
        self.y = False
        self.r = False
#change colour:
    def cc(self, g, y, r):
        self.g = g
        self.y = y
        self.r = r
    def schalten(self):
        if (self.g, self.y, self.r) == (True, False, False):
            self.y = True
        elif (self.g, self.y, self.r) == (True, True, False):
            (self.r, self.y) = False
            self.g = True
        else:
            self.r = False
            self.g = True
            self.y = False
    def ausgeben(self):
        print(self.g, self.y, self.r)

ampel1 = Ampel()
ampel1.cc(True, False, False)
