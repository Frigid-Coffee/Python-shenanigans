from chuckaluck import *

k = Konto(100)
s = Spielzahl(6)
wA = Wuerfel()
wB = Wuerfel()
wC = Wuerfel()

i = 0
while i < 100:
    if wA.augen == 6 or wB.augen == 6 or wC.augen == 6:
        if wA.augen == 6:
            k.einzahlen(1)
        if wB.augen == 6:
            k.einzahlen(1)
        if wC.augen == 6:
            k.einzahlen(1)
    else:
        k.auszahlen(1)
    wA.werfen()
    wB.werfen()
    wC.werfen()
    i = i + 1

# Ausgabe des Kontostands
print(k.stand)
