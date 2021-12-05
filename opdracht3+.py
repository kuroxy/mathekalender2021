def do_action(table,redbowl,blackbowl,move):
    if move==0:
        table-=1
        redbowl+=1
    elif move==1:
        table-=1
        blackbowl+=1
    elif move==2:
        table+=1
        redbowl-=1
    elif move==3:
        table+=1
        blackbowl-=1
    return table,redbowl,blackbowl



# starting conditions
table = 8
redbowl = 0
blackbowl = 0

#sequence get from opdracht3.py
sequence = [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 2, 3, 2, 2, 1, 0, 1, 0, 1]
print("T  R  B")
print(f"{table:<2} {redbowl:<2} {blackbowl:<2}")
for move in sequence:
    table,redbowl,blackbowl = do_action(table,redbowl,blackbowl,move)
    print(f"{table:<2} {redbowl:<2} {blackbowl:<2}")

"""
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 1, 0, 3, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 1, 0, 3, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 1, 0, 0, 3, 2]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 1, 0, 0, 3, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 0, 1, 0, 3, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0, 1, 2, 2]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0, 1, 2, 1]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 1, 2, 2, 3, 3, 2, 2]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 1, 2, 2, 3, 3, 2, 1]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 1, 2, 2, 3, 2, 3, 2]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 1, 2, 2, 3, 2, 3, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 2, 3, 2, 2, 1, 0, 1, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 2, 3, 2, 2, 1, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 1, 2, 3, 3, 2, 2, 1, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 1, 2, 3, 3, 2, 1, 2, 3, 2]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 1, 2, 2, 3, 2, 3, 0, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 1, 2, 2, 3, 0, 3, 2, 2, 2]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1, 1, 2, 2, 3, 0, 3, 2, 2, 1]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 3, 2, 2, 2, 1, 0, 1, 0, 3]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 3, 2, 2, 2, 1, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 3, 2, 2, 2, 1, 0, 0, 1, 2]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 3, 2, 2, 2, 1, 0, 0, 1, 1]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 3, 2, 2, 2, 1, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 3, 2, 1, 1, 2, 3, 3, 2, 2]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 3, 2, 1, 1, 2, 3, 3, 2, 1]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 3, 2, 1, 1, 2, 3, 2, 3, 2]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 3, 2, 1, 1, 2, 3, 2, 3, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 2, 3, 2, 2, 1, 0, 1, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 2, 3, 2, 2, 1, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 2, 1, 2, 3, 2, 3, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 1, 2, 3, 3, 2, 2, 1, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 1, 2, 3, 3, 2, 1, 2, 3, 2]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 1, 2, 3, 2, 2, 3, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 1, 2, 2, 3, 2, 3, 0, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 1, 2, 2, 3, 2, 3, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 1, 2, 2, 3, 0, 3, 2, 2, 2]
[0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 1, 2, 2, 3, 0, 3, 2, 2, 1]
"""