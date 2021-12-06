import time

win=3           # points for winning losing tieing...
loss=0
tie=1
 
options = [win,loss,tie]



def conditions(flist,rlist,notlist):          # coditions that were given That the score was 2 lower than the rank up ... etc
    scoreI = rlist[0] + rlist[1] + rlist[2] + rlist[3] + rlist[4]
    scoreF = flist[0] + rlist[5] + rlist[6] + rlist[7] + rlist[8]
    scoreG = flist[1] + flist[5] + rlist[9] + rlist[10] + rlist[11]
    scoreC = flist[2] + flist[6] + flist[9] + rlist[12] + rlist[13]
    scoreS = flist[3] + flist[7] + flist[10] + flist[12] + rlist[14]
    scoreW = flist[4] + flist[8] + flist[11] + flist[13] + flist[14]
    
    if scoreF==scoreI-2 and scoreG==scoreF-2 and scoreC==scoreG-2 and scoreS==scoreC-2 and scoreW==scoreS-2: # correct table
        # checking Possible answers
        # 1 Icetown beat Frostville and Glacierhampton.
        if not(rlist[0]==3 and rlist[1]==3):
            notlist.append(1)
        # 2 Icetown beat Coldbury and Winterfield.
        if not(rlist[2]==3 and rlist[4]==3):
            notlist.append(2)
        # 3 Frostville lost against Glacierhampton and won against Snowham.
        if not(rlist[5]==0 and rlist[7]==3):
            notlist.append(3)

        # 4 Glacierhampton beat Coldbury and Snowham.
        if not(rlist[9]==3 and rlist[10]==3):
            notlist.append(4)
        # 5 Glacierhampton beat Frostville and Coldbury.
        if not(flist[5]==3 and rlist[9]==3):
            notlist.append(5)
            
        # 6 Coldbury lost against Icetown and Glacierhampton.
        if not(flist[2]==0 and flist[9]==0):
            notlist.append(6)
        # 7 Coldbury lost against Snowham and won against Winterfield.
        if not(rlist[12]==0 and rlist[13]==3):
            notlist.append(7)
        # 8 Snowham lost against Icetown and Coldbury.
        if not(flist[3]==0 and flist[12]==0):
            notlist.append(8)
        # 9 Winterfield lost against Icetown and Frostville.
        if not(flist[4]==0 and flist[8]==0):
            notlist.append(9)
        #10 Winterfield lost against Coldbury and played draw against Glacierhampton.
        if not(flist[13]==0 and flist[11]==1):
            notlist.append(10)


def otherside (flist):  # inverting the list because it is linked with flist
    rlist = []
    for i in flist:
        if i == win:
            rlist.append(loss)
        elif i == loss:
            rlist.append(win)
        else:
            rlist.append(tie)
    return rlist

def solve(notlist):    # ja dit kan waarschijnlijk beter :) maar dit werkt ook
    for a in options:           # getting every possible combination only 3^15
        for b in options:
            for c in options:
                for d in options:
                    for e in options:
                        for f in options:
                            for g in options:
                                for h in options:
                                    for i in options:
                                        for j in options:
                                            for k in options:
                                                for l in options:
                                                    for m in options:
                                                        for n in options:
                                                            for o in options:
                                                                flist = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]
                                                                rlist = otherside(flist)
                                                                conditions(flist,rlist,notlist)
                                                                    

notlist = []
start_time = time.time()
solve(notlist)
for i in range(1,11):
    if i in notlist:
        print(f"{i} Is not true")
    else:
        print(f"{i} Is always true!")

print(f"It took {time.time()-start_time} seconds")







