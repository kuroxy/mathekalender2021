import time
#setup
pixies = ['' for _ in range(33)]
anwserlist = []

def get_possibility(pixies,index):  # get possitble color
    not_possibility = []
    if pixies[(index-1)%33] == "R" or pixies[(index+1)%33] == "R" :
        not_possibility.append("R")

    if pixies[(index-16)%33] == "R" or pixies[(index+16)%33] == "R":
        not_possibility.append("R")
    
    
    if "R" in not_possibility:
        return ["G"]
    return ["G","R"]


def solve(pixies,index): # solving using recursion
    global anwserlist
    if index==33:
        anwserlist.append(pixies)
        return

    for color in get_possibility(pixies,index):
        temp = pixies.copy()
        temp[index] = color
        solve(temp,index+1)

begintime =time.time()
solve(pixies,0) # getting every valid sequence

amount = 0  # sorting/ so get the biggest amount of reds
answer = []
for i in anwserlist:
    am = sum(j == "R" for j in i)
    if am > amount:
        amount=am
        answer=i

print(amount)
print(answer)
print(f"It took {time.time()-begintime} seconds")