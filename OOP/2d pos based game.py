import random as r

tdic = {
    "forrest": ["You come accros a dence forrest", "axe"],
    "dessert": ["You come accros an arid dessert wasteland with nothing in sight"],
    "lake": ["A tranquil lake with a small jetty lies in your path"]
    }

tlist = ["forrest", "dessert", "lake", "abandoned cabin"]

mapl = []

class Player():
    def __init__(self, pos = [0,0], inv = ["sword","torch"]):
        self.inv = inv
        self.pos = pos
    def move(self, card):
        if card in {"n", "s", "w", "e"}:
            if card == "n":
                if (self.pos[0] + 1) >= 0 and (self.pos[0] + 1) < len(mapl):
                    self.pos[0] -= 1
            elif card == "s":
                if (self.pos[0] + 1) >= 0 and (self.pos[0] + 1) < len(mapl):
                    self.pos[0] += 1
            elif card == "e":
                if (self.pos[1] + 1) >= 0 and (self.pos[1] + 1) < len(mapl[self.pos[0]]):
                    self.pos[1] -= 1
            else:
                if (self.pos[1] + 1) >= 0 and (self.pos[1] + 1) < len(mapl[self.pos[0]]):
                    self.pos[1] += 1
        else:
            print("please input either 'n', 's', 'e' or 'w'")
        
    def gpos(self):
        return self.pos
    def gbiom(self ,y, x ):
        return mapl[y][x]
        

class Tera():
    def __init__(self, biom):
        self.biom = biom
    def getFlav(self, obj):
        return
        
f = Tera("forrest")
d = Tera("dessert")
l = Tera("lake")
cabin = Tera("a_cabin")

def tgen(length, width):
    for y in range(length):
        mapl.append([])
        for x in range(width):
            biom = tlist[r.randint(0,3)]
            mapl[y].append(biom)
    
def game():
    play = "j"
    length = int(input("What should the length of this wonderfull land be? "))
    width = int(input("And its width? "))
    player = Player([round(length/2, 0), round(width/2, 0)])
    tgen(length, width)
    while play == "j":

        cardin = input("Where will thy step?")
        player.move(cardin)
        print(tdic[player.gbiom(self.pos[0], self.pos[1])][0])
        
        
tgen(2,2)
a = Player()
print(a.gpos())
a.move("n")
print(a.gpos())
        
