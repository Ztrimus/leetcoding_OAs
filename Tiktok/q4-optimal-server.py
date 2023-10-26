'''
-----------------------------------------------------------------------
Author: Saurabh Zinjad
Developer Email: zinjadsaurabh1997@gmail.com
File: optimal-server-q4.py
Creation Time: Oct 25th 2023 10:50 pm
Copyright (c) 2023 Saurabh Zinjad. All rights reserved | GitHub: Ztrimus
-----------------------------------------------------------------------
'''
import math
def optimal_server(price):
    n = len(price)
    result = 0
    
    diff = []
    diff_sum = 0
    
    left_diff = []
    right_diff = []

    for i in range(n-1):
        value = abs(price[i] - price[i+1])
        diff_sum += value
        diff.append(value)
        left_diff.append(abs(price[i]//2 - price[i+1]))
        right_diff.append(abs(price[i] - price[i+1]//2))
    
    result = diff_sum
    
    print(f"diff: {diff}")
    
    for i in range(n-1):
        current_diff = diff_sum - diff[i]
        if i-1 >= 0:
            current_diff -= diff[i-1]
            current_diff += right_diff[i-1]
        if left_diff[i]:
            current_diff += left_diff[i]
            
        result = min(current_diff, result)
        print(f"current_diff: {current_diff}")
    
    last_diff = result - diff[-1] + right_diff[-1]
    print(f"current_diff: {last_diff}")
    return min(last_diff, result)

print("Result: ", optimal_server(price=[1,4,1]), "\n\n")
print("Result: ", optimal_server(price=[22,18,57]), "\n\n")
print("Result: ", optimal_server(price=[12,14,24,12]), "\n\n")
print("Result: ", optimal_server(price=[0,0,0,0]), "\n\n")
print("Result: ", optimal_server(price=[14,14,14,14]), "\n\n")
print("Result: ", optimal_server(price=[1,2,3,4,5,6]), "\n\n")