from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        neighbors = defaultdict(List)
        
        for s, e, w in times:
            neighbors[s] = (e, w)
        
        shortest = {}
        minHeap = [(0, k)]

        while minHeap:
            n1, w1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue

            shortest[n1] = w1

            for n2, w2 in neighbors[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (n2, w1+w2))
        
        return shortest

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

dd = Solution()
print(dd.networkDelayTime(times, n ,k))