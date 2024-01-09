def minchair(sim):
    l = []
    for i in range(len(sim)):
        tot, avl = 0, 0
        for k in sim[i]:
            if k == 'C':
                if avl == 0:
                    tot+=1
                else:
                    avl-=1
            if k == 'R':
                avl+=1
            if k == 'U':
                if avl == 0:
                    tot+=1
                else:
                    avl-=1
            if k == 'L':
                avl+=1
        l.append(tot)
    return l

# sim = ["CCRUCL", "CRUC", "CCCC"]
# print(minchair(sim))

# sim = ["CCCRRR", "CC", "CCRURC"]
# print(minchair(sim))

sim = ["CRCRCRUUCURUCRUCLCR", "CC", "CCRURC"]
print(minchair(sim))




