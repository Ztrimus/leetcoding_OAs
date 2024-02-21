'''
-----------------------------------------------------------------------
File: playground.py
Creation Time: Feb 5th 2024, 2:51 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''


import math

class MedianFinder(object):

    def __init__(self):
        self.arr = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.arr.append(num)
        

    def findMedian(self):
        """
        :rtype: float
        """
        len_arr = len(self.arr)
        first = int(math.floor(len_arr/2))

        if len_arr%2:
            result = self.arr[first]
        else:
            result = (self.arr[first] + self.arr[first-1])/2
        
        return result
        
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian())