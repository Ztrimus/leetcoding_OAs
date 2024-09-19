"""
100380. Maximum Multiplication Score

You are given an integer array a of size 4 and another integer array b of size at least 4.

You need to choose 4 indices i0, i1, i2, and i3 from the array b such that i0 < i1 < i2 < i3. Your score will be equal to the value a[0] * b[i0] + a[1] * b[i1] + a[2] * b[i2] + a[3] * b[i3].

Return the maximum score you can achieve.

 

Example 1:

Input: a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7]

Output: 26

Explanation:
We can choose the indices 0, 1, 2, and 5. The score will be 3 * 2 + 2 * (-6) + 5 * 4 + 6 * 2 = 26.

Example 2:

Input: a = [-1,4,5,-2], b = [-5,-1,-3,-2,-4]

Output: -1

Explanation:
We can choose the indices 0, 1, 3, and 4. The score will be (-1) * (-5) + 4 * (-1) + 5 * (-2) + (-2) * (-4) = -1.

 

Constraints:

a.length == 4
4 <= b.length <= 105
-105 <= a[i], b[i] <= 105
"""

from typing import List, Tuple
from functools import lru_cache
from math import inf

class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        b1, b2, b3, b4 = -inf, -inf, -inf, -inf
        for x in b:
            b4 = max(b4, b3 + x * a[3])
            b3 = max(b3, b2 + x * a[2])
            b2 = max(b2, b1 + x * a[1])
            b1 = max(b1, x * a[0])
        return b4


    def maxScore_(self, a: List[int], b: List[int]) -> int:
        
        @lru_cache(maxsize=None)
        def dp(a: Tuple[int, ...], b: Tuple[int, ...]) -> int:
            max_cal = -inf
            
            if len(a) > 0:
                for i in range(len(b) - len(a) + 1):
                    res = a[0] * b[i] + dp(a[1:], b[i+1:])
                    max_cal = max(max_cal, res)
                return max_cal
            else:
                return 0
        
        return dp(tuple(a), tuple(b))

obj = Solution()

for testcase in [
    [[3,2,5,6], [2,-6,4,-5,-3,2,-7], 26],
    [[-1,4,5,-2], [-5,-1,-3,-2,-4], -1],
    [[-630,697,712,-837], [8,-26,-383,-297,59,340,569,-858,691,109,274,-87,-765,-252,-814,-280,994,514,-43,551,187,-266,-448,568,-872,165,-316,351,-824,-856,-525,402,702,938,-238,101,-13,161,881,-165,171,-908,-998,222,142,-863,-851,-669,105,523,924,377,886,-559,-517,261], 0],
    ]:
    print()
    print(f"a={testcase[0]}, b={testcase[1]} :: {testcase[2]} == {obj.maxScore(testcase[0], testcase[1])}")