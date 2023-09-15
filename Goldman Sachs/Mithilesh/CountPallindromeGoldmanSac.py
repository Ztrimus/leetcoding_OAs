#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countPalindromes' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def countPalindromes(s):
    # Write your code here
    def check(l,r):
        count = 0
        while l>=0 and r<len(s) and s[l] == s[r]:
            count+=1
            l-=1
            r+=1
        return count
    
    count = 1
    for i in range(len(s)-1):
        # odd
        count += check(i,i)
        # even
        count += check(i,i+1)
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = countPalindromes(s)

    fptr.write(str(result) + '\n')

    fptr.close()
