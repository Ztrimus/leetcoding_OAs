'''
-----------------------------------------------------------------------
File: playground.py
Creation Time: Feb 5th 2024, 2:51 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''

def countOrders(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1 
    return n * (2*(n-1)+1) * countOrders(n-1) % (10**9 + 7)

print(countOrders(3))