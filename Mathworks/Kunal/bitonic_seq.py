'''
-----------------------------------------------------------------------
File: bitonic_seq.py
Creation Time: Feb 20th 2024, 9:20 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''

def is_bitonic(arr, start, end):
    only_increasnig = True

    if arr[start+1] <= arr[start]:
        return False
    for i in range(start+1, end):
        if arr[i] == arr[i + 1]:
            return False
        if arr[i] > arr[i + 1]:
            only_increasnig = False
    if only_increasnig:
        return False
    return True

def count_bitonic(arr, n):
    count = 0
    for interval in range(n, 2, -1):
        for iter in range(n-interval+1):
            j = iter+interval-1
            print(f"{arr[iter:j+1]}:{is_bitonic(arr, iter, j)}")
            if is_bitonic(arr, iter, j):
                count += 1
    return count

print(count_bitonic([1,2,3,2,1], 5))
# print(count_bitonic([1,2,3,1], 4))
# print(count_bitonic([100,50,50,100], 4))