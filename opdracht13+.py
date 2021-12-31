import math
from PIL import Image, ImageDraw
import pickle


def create_painting(world,name):

    # creating new Image object
    img = Image.new("RGB", (110, 110))
    
    # create rectangle image
    img1 = ImageDraw.Draw(img)  


    for i in range(11**2):
        pos = [i % 11,math.floor(i/11)]
        x = pos[0]
        y=pos[1]
        filltype = world[y][x]
        if filltype==1:
            img1.rectangle([(x*10,y*10),(x*10+10,y*10+10)], fill ="white", outline ="black")

        if filltype==2:
            img1.rectangle([(x*10,y*10),(x*10+20,y*10+20)], fill ="blue", outline ="black")
            world[y][x+1] = 0
            world[y+1][x] = 0
            world[y+1][x+1] = 0
        
        if filltype==3:
            img1.rectangle([(x*10,y*10),(x*10+20,y*10+10)], fill ="yellow", outline ="black")
            world[y][x+1] = 0


        if filltype==4:
            img1.rectangle([(x*10,y*10),(x*10+10,y*10+20)], fill ="red", outline ="black")
            world[y+1][x] = 0


    img.save(name,"PNG")


with open("worlds125600.pcl", 'rb') as pickle_file:
    worlds = pickle.load(pickle_file)


create_painting(worlds[-1],f"opdr13/World_{125600-1}.png")

""" 
for i in range(len(worlds)):
    create_painting(worlds[i],f"opdr13/World_{i}.png")


world = [[3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 4],
[1, 4, 2, 2, 2, 2, 2, 2, 2, 2, 4],
[4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 4],
[4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 4],
[4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 4],
[4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 4],
[4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 4],
[4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 4],
[4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 4],
[4, 3, 3, 3, 3, 3, 3, 1, 2, 2, 4],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1]]


create_painting(world,f"opdr13/4world.png")"""