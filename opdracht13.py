#13 Mondrian
import math
import time
import copy
import pickle

world = [[0 for _ in range(11)] for _ in range(11)]

world[0][9] = 1


world[7][1] = 1
world[10][0] = 1


def checkputsquare(world,lefttop):
    if lefttop[0] < 0 or lefttop[0] > 9:
        return False

    if lefttop[1] < 0 and lefttop[1] > 9:
        return False
    x = lefttop[0]
    y = lefttop[1]
    if any([world[y][x],world[y][x+1],world[y+1][x],world[y+1][x+1]]):
        return False
    
    world[y][x]=2
    world[y][x+1]=2
    world[y+1][x]=2
    world[y+1][x+1]=2
    return True


def checkputbarhorizontal(world,lefttop):
    if lefttop[0] < 0 or lefttop[0] > 10:
        return False

    if lefttop[1] < 0 or lefttop[1] > 9:
        return False
    x = lefttop[0]
    y = lefttop[1]
    if any([world[y][x],world[y][x+1]]):
        return False
    
    world[y][x]=3
    world[y][x+1]=3
    return True

def checkputbarvertical(world,lefttop):
    if lefttop[0] < 0 or lefttop[0] > 9:
        return False

    if lefttop[1] < 0 or lefttop[1] > 10:
        return False
    
    x = lefttop[0]
    y = lefttop[1]
    if any([world[y][x],world[y+1][x]]):
        return False
    
    world[y][x]=4
    world[y+1][x]=4
    return True


def getavailable(world,pos):
    options = [2,3,4]
    
    if pos[0] > 9:
        options.remove(2)
        options.remove(3)

    if pos[1] > 9:
        if 2 in options:
            options.remove(2)
        options.remove(4)

    x = pos[0]
    y = pos[1]
    if 2 in options and any([world[y][x],world[y][x+1],world[y+1][x],world[y+1][x+1]]):
        options.remove(2)
    
    if 3 in options and any([world[y][x],world[y][x+1]]):
        options.remove(3)

    if 4 in options and any([world[y][x],world[y+1][x]]):
        options.remove(4)
    
    return options


def placesquare(world,pos,num=2):
    x = pos[0]
    y = pos[1]
    world[y][x]=num
    world[y][x+1]=num
    world[y+1][x]=num
    world[y+1][x+1]=num
    return True


def placehorizontal(world,pos,num=3):
    x = pos[0]
    y = pos[1]
    world[y][x]=num
    world[y][x+1]=num
    return True


def placevertical(world,pos,num=4):
    x = pos[0]
    y = pos[1]
    world[y][x]=num
    world[y+1][x]=num
    return True


def zerosurround(pos,world):
    x = pos[0]
    y = pos[1]
    if x != 0 and world[y][x-1]==0:
        return True
    if x != 10 and world[y][x+1]==0:
        return True
    
    if y != 0 and world[y-1][x]==0:
        return True
    if y != 10 and world[y+1][x]==0:
        return True
    return False

def possible(world):
    for i in range(11**2):
        pos = [i % 11,math.floor(i/11)]
        if world[pos[1]][pos[0]] != 0:
            continue

        if not zerosurround(pos,world):
            return False
    return True

def move(world,pos,move,num=None):
    if num!=None:
        if move == 2:
            placesquare(world,pos,num)
        if move == 3:
            placehorizontal(world,pos,num)
        if move == 4:
            placevertical(world,pos,num)
        return
    
    if move == 2:
        placesquare(world,pos)
    if move == 3:
        placehorizontal(world,pos)
    if move == 4:
        placevertical(world,pos)
    return


def amounttwo(world):
    twos = 0
    for i in world:
        for j in i:
            if j==2:
                twos+=1
    return twos






def goodprint(world):
    for i in world:
        print(i)


bestamounttwo = 0
bestworld = []
latesttime = 0
bestworlds = []
starttime = time.time()



def solver(world,currentindex):
    global bestamounttwo
    global bestworld
    global latesttime
    global starttime

    if currentindex == 11**2:
        amount = amounttwo(world)

        if amount == 17*4:
            goodworld = copy.deepcopy(world)
            bestworlds.append(goodworld)
            print(len(bestworlds))
            if len(bestworlds)%100 ==0:
                """
                with open(f"worlds{len(bestworlds)}.pcl", 'wb') as pickle_file:
                    pickle.dump(bestworlds,pickle_file)
                """ #turned off because isnt nessarely if you dont want to run overnight (or you dont want new files on your pc)

                print(f"pickle dump took {len(bestworlds)} {time.time()-starttime} secs")

        if amount > bestamounttwo:
            goodprint(world)
            print(f"BEST {int(amount/4)}")
            bestworld = copy.deepcopy(world)
            bestamounttwo = amount

        else:
            
            if time.time()-30 > latesttime:
                latesttime = time.time()
                goodprint(world)
                print(f"TIME {int(amount/4)}")

                goodprint(bestworld)
                print(f"BEST ^^^^^^^^^ 4")
        return
    
    pos = [currentindex % 11,math.floor(currentindex/11)]

    if (121-currentindex)/4 +amounttwo(world)/4 < 17:
        return

    if world[pos[1]][pos[0]] !=0:
        solver(world,currentindex+1)

    for i in getavailable(world,pos):

        move(world,pos,i)
        if not possible(world):
            move(world,pos,i,0)
            continue
  
        solver(world,currentindex+1)

        move(world,pos,i,0)

    return



world = [list(r) for r in zip(*world[::-1])]
world = [list(r) for r in zip(*world[::-1])]
world = [list(r) for r in zip(*world[::-1])]

solver(world,0)


print(bestworld)
print(bestamounttwo)