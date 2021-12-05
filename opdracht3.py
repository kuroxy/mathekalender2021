import time

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


def get_possible_moves(table,redbowl,blackbowl,rb):
    possible_moves = [0,1,2,3]

    if table==0:
        possible_moves.remove(0)
        possible_moves.remove(1)
    
    if redbowl==0:
        possible_moves.remove(2)

    if blackbowl==0:
        possible_moves.remove(3)
    
    truepossible = []
    for move in possible_moves:
        _,r,b = do_action(table,redbowl,blackbowl,move)
        

        if r>=b and not end_condition(r,b,rb):
            truepossible.append(move)


    return truepossible
    
def end_condition(redbowl,blackbowl,rb):
    if [redbowl,blackbowl] in rb:
        return 1
    return 0


def solve(table,redbowl,blackbowl,RB_quantities,steps):
    global endconditions
    moves = get_possible_moves(table,redbowl,blackbowl,RB_quantities)
    if len(moves)==0:
        endconditions.append(steps)
        return 1



    for move in moves:
        t,r,b = do_action(table,redbowl,blackbowl,move)
        rb = RB_quantities.copy()
        rb.append([redbowl,blackbowl])
        s = steps.copy()
        s.append(move)
        
        solve(t,r,b,rb,s)

#starting conditions
table=7
redbowl = 0
blackbowl = 0

# keeping track of R&B combinations already had for endcondition
RB_quantities = []

endconditions = []
#moves 
# 0 : table to redbowl
# 1 : table to blackbowl
# 2 : redbowl to table
# 3 : blackbowl to table


start_time = time.time()
solve(table,redbowl,blackbowl,[],[])

endconditions.sort(key=len)
endconditions.reverse()
#print(endconditions[0])
print(f"table start {table}")
for i in range(20):
    print(endconditions[i])

print(f"It took {time.time()-start_time} seconds")

# time stamps

#9 : 0.36seconds
#10: 4.43seconds
#11: 81.4seconds#

