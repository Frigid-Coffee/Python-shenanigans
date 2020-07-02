import random as r
from math import factorial

L = [1,2,3]


def vorhanden(Liste, obj):
    for i in range(len(Liste)):
        if Liste[i] == obj:
            return False

def permutate(Liste):
    permutations = []
    for x in range(factorial(len(Liste))):
        p = []
        for x in range(len(Liste)):
            rndNum = r.randint(0, len(Liste))
            if vorhanden(p, rndNum):
                p.append(rndNum)
            else:
                permutate(Liste)
            permutations.append(p)

            
permutate(L)
print
