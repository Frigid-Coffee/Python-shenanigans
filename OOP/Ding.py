

class Ding:   
    def __init__(self, volumen, symbol):
        self.volumen = volumen
        self.symbol = symbol
        self.dichte = {'Fe': ('Eisen', 7.87),
              'Au': ('Gold', 19.32),
              'Ag': ('Silber', 10.5)}
 
    def getMasse(self):
        masse = self.volumen * self.dichte[self.symbol][1]
        return (masse)
        
        
    def getVolumen(self):
        return(self.volumen)

    def __str__(self):
        print(self.getVolumen(), "cm^3") 
        print(self.getMasse(),"g")
        print(self.symbol, self.dichte[self.symbol])

a = Ding(10, "Fe") 
print(a)
