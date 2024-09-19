'''
-----------------------------------------------------------------------
File: TP/rotated_binary_search.py
Creation Time: Aug 29th 2024, 11:39 am
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''

from typing import List


def search(nums: List[int], target: int) -> int:
    if len(nums) <=0:
        return -1
    
    l,r = 0, len(nums)-1

    while l <= r:
        if l == r:
            if target == nums[l]:
                return l
            else:
                return -1
        else:
            mid = int((l+r)/2)
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                if target < nums[l]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if target > nums[r]:
                    l = mid+1
                else:
                    r = mid-1
    return -1

for testcase in [
    [[4,5,6,7,8,1,2,3], 8, 4],
    [[4,5,6,7,0,1,2], 0, 4],
    [[1,3], 3, 1],
    [[1,3], 4, -1]
]:
    print(f"nums: {testcase[0]}; target: {testcase[1]} => {search(testcase[0], testcase[1]) == testcase[2]}")