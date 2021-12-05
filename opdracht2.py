import random
from collections import Counter
import time

starttime = time.time()
thelist = []

for _ in range(1000): # the higher the more accurate the answer will be, but 1000 is already pretty close
    seq = ""
    seq += "K" if random.random() <= .75 else "M"   # random coinflip coin A
    seq += "M" if random.random() <= .75 else "K"   # random coinflip coin B
    thelist.append(seq)# add to the list to keep track of the chances

counted = Counter(thelist)  # counting all possibilities
print(f"total amount : {len(thelist)}") # total flips to go off
le = len(thelist)
print(f"KK amount : {counted['KK']/le} {counted['KK']}" )   #  chance of two heads, amount of two heads flipped
print(f"KM amount : {counted['KM']/le} {counted['KM']}" )   #  chance of head-tails, amount of head-
print(f"MK amount : {counted['MK']/le} {counted['MK']}" )   #  chance of tails-head, amount of tails-head
print(f"MM amount : {counted['MM']/le} {counted['MM']}" )   #  chance of two tails, amount of two tails flipped

print(f"The Answer : {counted['KM']/(counted['KM']+counted['MK'])}")    # same process as other calculation, we want to know KM so we divide it by total posibilities. 
print(f"It took {round(time.time()-starttime,3)} seconds")