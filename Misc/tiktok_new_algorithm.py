'''
File: tiktok_new_algorithm.py
Project: Coding
File Created: 14th Oct 2023 10:56 pm, Saturday
Author: Saurabh Zinjad (GitHub: Ztrimus)
Email: zinjadsaurabh1997@gmail.com

Copyright (c) 2023 Saurabh Zinjad
'''
import collections


def newAlogFun(arr):
    idx = collections.defaultdict(list)
    n = len(arr)
    for i,j in enumerate(arr):
        idx[j]+=[i]
        
    res=[float('inf')]*n
        
    for num in idx:
        x=[-1]+idx[num]+[n]
        y=max(j-i for i,j in zip(x[:-1],x[1:]))
        res[y-1]=min(res[y-1],num)
            
    for i in range(1,n):
        res[i]=min(res[i],res[i-1])     
    
    return [i if i !=float('inf') else -1 for i in res]


print(newAlogFun([2,4,2,3,5]))
print(newAlogFun([3,2,3,1]))
