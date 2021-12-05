thelist = []
for i in range(17):
    for j in range(17):
        if i+j<= 16:
            thelist.append([i,j])

print(thelist)
print(len(thelist))