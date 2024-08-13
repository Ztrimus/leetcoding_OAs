'''
-----------------------------------------------------------------------
File: TP/jump_game_II.py
Creation Time: Jul 20th 2024, 7:26 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''

from typing import List
import numpy as np

# print(jump([2,3,1,1,4])) # Output: 2
# print(jump([3,2,1])) # Output: 1

def jump(nums: List[int]) -> int:
    crnt_idx = 0
    jumps = 0
    n = len(nums)

    while crnt_idx < n-1:
        hgh_jmp = nums[crnt_idx]
        lft = crnt_idx+1
        rght = min(crnt_idx+1+hgh_jmp, n)
        if rght == n:
            return jumps+1
        nxt_psble_jumps = [jmp+idx if jmp > 0 else 0 for idx, jmp in enumerate(nums[lft:rght])]
        nxt_idx = crnt_idx + (np.argmax(nxt_psble_jumps)+1)
        crnt_idx = min(nxt_idx, n)
        jumps += 1
    
    return jumps

print(jump([2,3,1,1,4])) # Output: 2