#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxMin' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY operations
#  2. INTEGER_ARRAY x
#
import heapq
def maxMin(operations, x):
    # Write your code here
    maxHeap = []
    minHeap = []
    nums = []
    
    res = []
    for i in range(len(operations)):
        operation = operations[i]
        value = x[i]
        
        if operation == "push":
            nums.append(value)
            
            heapq.heappush(maxHeap, -value)
            heapq.heappush(minHeap, value)
        elif operation == "pop":
            nums.remove(value)
            
            maxHeap.remove(-value)
            minHeap.remove(value)
            
            heapq.heapify(maxHeap)
            heapq.heapify(minHeap)
        
        maxVal = -maxHeap[0] if maxHeap else 0
        minVal = minHeap[0] if minHeap else 0
        product = maxVal*minVal
        
        res.append(product)
    
    return res
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    x_count = int(input().strip())

    x = []

    for _ in range(x_count):
        x_item = int(input().strip())
        x.append(x_item)

    result = maxMin(operations, x)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
