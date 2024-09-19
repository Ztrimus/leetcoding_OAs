from typing import List
from itertools import combinations

class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        max_score = float('-inf')
        
        for combo in combinations(range(n), 4):
            score = sum(a[i] * b[idx] for i, idx in enumerate(combo))
            max_score = max(max_score, score)
        
        return max_score

# Test the solution
obj = Solution()

for testcase in [
    [[-630,697,712,-837], [8,-26,-383,-297,59,340,569,-858,691,109,274,-87,-765,-252,-814,-280,994,514,-43,551,187,-266,-448,568,-872,165,-316,351,-824,-856,-525,402,702,938,-238,101,-13,161,881,-165,171,-908,-998,222,142,-863,-851,-669,105,523,924,377,886,-559,-517,261], 2736540],
    [[3,2,5,6], [2,-6,4,-5,-3,2,-7], 26],
    [[-1,4,5,-2], [-5,-1,-3,-2,-4], -1]
]:
    result = obj.maxScore(testcase[0], testcase[1])
    print(f"a={testcase[0]}, b={testcase[1]} :: Expected: {testcase[2]}, Got: {result}")
    assert result == testcase[2], f"Test case failed: expected {testcase[2]}, got {result}"

print("All test cases passed!")