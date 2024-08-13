'''
-----------------------------------------------------------------------
File: playground.py
Creation Time: Feb 5th 2024, 2:51 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''

from typing import List
from collections import defaultdict

def longestConsecutive(nums: List[int]) -> int:
        have_next_no = defaultdict(int)
        long_len = 0

        for i in nums:
            if i not in have_next_no:
                next_i=i
                while (next_i:=next_i+1) in nums:
                    if i in have_next_no:
                        have_next_no[i] += 1
                    else:
                        have_next_no[i] = 1
                    if next_i in have_next_no:
                        have_next_no[i] += have_next_no[next_i]
                        break
                long_len = max(long_len, have_next_no.get(i,1))
        
        return long_len+1

num
print(longestConsecutive(num)) # Output: 9