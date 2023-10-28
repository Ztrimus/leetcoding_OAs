'''
-----------------------------------------------------------------------
Author: Saurabh Zinjad
Developer Email: zinjadsaurabh1997@gmail.com
File: q5-idle-server.py
Creation Time: Oct 26th 2023 12:04 am
Copyright (c) 2023 Saurabh Zinjad. All rights reserved | GitHub: Ztrimus
-----------------------------------------------------------------------
'''

def minimumcost(data, k):
    n = len(data) // 2
    data = sorted(enumerate(data, 1), key=lambda x: x[1])
    min_cost = float('inf')
    
    for i in range(1, n):
        total_capacity = data[i][1] + data[i + n][1]
        if total_capacity >= k:
            min_cost = min(min_cost, data[i][0] - 1)
    
    return min_cost if min_cost != float('inf') else -1

# print(minimumcost([3,1,5,2], 6)) 
print(minimumcost([2,5,1,7,3,8], 14)) 
print(minimumcost([10,30,15,25], 100)) 