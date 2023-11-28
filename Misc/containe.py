# Container with most water
from typing import List

def maxArea(height: List[int]) -> int:
    right,left = len(height)-1,0
    rightvalue = height[right]
    leftvalue = height[left]
    maxarea = abs(right-left)*min(rightvalue,leftvalue)
    while (left<right):
        if(leftvalue<height[left+1]):
            left+=1
            leftvalue = height[left]

        if(height[right-1]>rightvalue):
            right-=1
            rightvalue = height[right]
        
        area = abs(right-left)*min(rightvalue,leftvalue) 
        if(area>maxarea):
            maxarea = area
    return maxarea

maxArea([1,8,6,2,5,4,8,3,7])