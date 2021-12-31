import itertools
import time
import math

timestart = time.time()
allcombinations = list(itertools.product('123', repeat=10))

def count(listin):
    red = 0
    silver =0
    green = 0

    for i in listin:
        if i == "1":
            red+=1
        elif i == "2":
            silver+=1
        elif i == "3":
            green+=1
    
    return [red,silver,green]


combi = [count(i) for i in allcombinations]

dup_free = []
for x in combi:
    if x not in dup_free:
        dup_free.append(x)

print(dup_free)
print(len(dup_free))


#11d
totalsum = 0
for i in range(9+1): # from 0-9
    print(((math.comb(9,i))/(2**9))**2)
    totalsum+= ((math.comb(9,i))/(2**9))**2
print(totalsum)


print(f"It took {time.time()-timestart} seconds")


from math import comb
