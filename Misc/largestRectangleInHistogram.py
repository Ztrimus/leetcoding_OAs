from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        level = 0
        max_rect = 0
        max_heights = max(heights)+1

        while sum(heights) > 0:
            block_max_len = 0
            block_min_height = max_heights
            for i in heights:
                if i == 0:
                    block_area = (block_min_height + level)*block_max_len
                    max_rect = max(max_rect, block_area)
                    block_max_len = 0
                    block_min_height = max_heights
                else:
                    block_max_len += 1
                    block_min_height = min(i,block_min_height)
            
            block_area = (block_min_height + level)*block_max_len
            max_rect = max(max_rect, block_area)
            level += 1
            heights = [max(i-1, 0) for i in heights]

        return max_rect

sol = Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3]))



