'''
File: trapping_rain_water_2_pointer_leetcode.py
Project: Coding
File Created: 2nd Oct 2023 7:43 pm, Monday
Author: Saurabh Zinjad (GitHub: Ztrimus)
Email: zinjadsaurabh1997@gmail.com

Copyright (c) 2023 Saurabh Zinjad
'''
# https://leetcode.com/problems/trapping-rain-water/description/

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        block_weights = 0
        block_water_weights = 0
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0

        while height[l] == 0:
            l+=1

        while height[r] == 0:
            r-=1

        while l <= r:

            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])

            if l != r:
                if l_max > r_max:
                    block_weights += height[r]
                    block_water_weights += r_max
                    r -= 1
                elif l_max < r_max:https://www.youtube.com/watch?v=Y0sibhk0fUk
                    block_weights += height[l]
                    block_water_weights += l_max
                    l += 1
                else:
                    block_weights += height[l] + height[r]
                    block_water_weights += l_max + r_max
                    l+=1
                    r-=1
            else:
                block_weights += height[l]
                block_water_weights += min(l_max, r_max)
                l+=1

        return block_water_weights - block_weights
    
water_obj = Solution()
print(water_obj.trap([0,1,0,2,1,0,1,3,2,1,2,1]))