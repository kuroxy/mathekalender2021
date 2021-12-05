import itertools
 

searchroute = "HFBDIGACE"
routepoints = "".join(sorted(searchroute))    # sort the route so we get it in alphabetical order

nums = list(routepoints)
permutations = list(itertools.permutations(nums))
all_permutations = [''.join(permutation) for permutation in permutations] # All permutations are in this list ["ABCDEFGH","ABCDEFHG"....,"IHGFEDCAB", "IHGFEDCBA"]
#print(all_permutations)

anwser = all_permutations.index(searchroute)+1  
# Get the position of the searchroute in the list since itertools.permutations is the permution like in the assignment, we can just this.
# We add 1 to the answer because in python lists starts at 0 and in the assignment the routes starts at 1
print(anwser) 
# 308515
