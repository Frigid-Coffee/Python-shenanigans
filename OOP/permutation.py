import random as r
from math import factorial

a = [1,2,3]

def vorhanden(Liste, obj):
    for i in range(len(Liste)):
        if Liste[i] == obj:
            return False

def permutate(Liste):
    combintaions = []
    perm = []
    a = 0
    for x in range(len(Liste)):
        print("x =",x)
        if x%len(Liste) == 0:
            a += 1
        for y in range(factorial(len(Liste[a:]))):
            print(Liste[x])
            perm.append([Liste[x]])
            perm[x].append(Liste[y+1])
            print(perm)
            print("y = ", y)
            


permutate(a)
