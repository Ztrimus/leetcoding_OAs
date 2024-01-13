import math
def getStep(bxs):
    max, min = 0, math.inf
    max_i, min_i = 0, 0

    iter = 0
    
    while abs(max-min) > 1:
        for i in range(len(bxs)):
            if bxs[i] > max:
                max = bxs[i]
                max_i = i
            if bxs[i] < min:
                min = bxs[i]
                min_i = i
        
        bxs[max_i] -= 1
        bxs[min_i] += 1
        max, min = 0, math.inf
        iter += 1
    
    return iter
        
print(getStep([5,5,8,7])) # 2
print(getStep([2,4,1])) # 1
print(getStep([4,4,4,4])) # 0

 