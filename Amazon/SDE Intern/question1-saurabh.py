from queue import PriorityQueue

def getMax(reward):
    pq = PriorityQueue()
    max, iter = 0, 0

    for r in reward:
        pq.put(-1*r)

    for i in range(len(reward)):
        item = (-1*pq.get() - iter)
        max += item if item > 0 else 0
        iter += 1
    
    return max

print(getMax([5,2,2,3,1])) # 7
print(getMax([5,5,5])) # 12
print(getMax([1,3,5,2,4])) # 9