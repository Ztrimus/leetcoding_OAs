'''
File: ibm_frontend_q1_final_data_update.py
Project: Mithiliesh
File Created: 3rd Oct 2023 11:32 pm, Tuesday
Author: Saurabh Zinjad (GitHub: Ztrimus)
Email: zinjadsaurabh1997@gmail.com

Copyright (c) 2023 Saurabh Zinjad
'''

def solve(arr, updates):
    n = len(arr)
    flag = [0] * n
    
    for update in updates:
        # 1-based index
        flag[update[0] - 1] += 1
        if update[1] < n:
            flag[update[1]] -= 1
    
    for i in range(n):
        if i > 0:
            flag[i] += flag[i - 1]
        
        # if we have to change odd times then change sign
        if flag[i] % 2 == 1:
            arr[i] = -arr[i]

if _name_ == "_main_":
    updates = [[1, 4], [3, 5],[1, 4], [3, 5],[2,3]]
    data = [3,1,3,0,7]
    solve(data, updates)
    print(data)