import bisect
from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted(nums)
        
        # 1. Component tracking to filter out unreachable queries
        comp = [0] * n
        c = 0
        for i in range(1, n):
            if arr[i] - arr[i - 1] > maxDiff:
                c += 1
            comp[i] = c
            
        # 2. Binary lifting table preparation
        LOG = 17
        up = [[0] * n for _ in range(LOG)]
        
        j = 0
        for i in range(n):
            while j + 1 < n and arr[j + 1] - arr[i] <= maxDiff:
                j += 1
            up[0][i] = j
            
        for k in range(1, LOG):
            prev = up[k - 1]
            curr = up[k]
            for i in range(n):
                curr[i] = prev[prev[i]]
                
        # 3. Answer queries
        ans = [0] * len(queries)
        for i, (u, v) in enumerate(queries):
            # Same exact node -> 0 distance
            if u == v:
                ans[i] = 0
                continue
                
            val1 = nums[u]
            val2 = nums[v]
            
            # Since the graph is undirected, always jump left to right
            if val1 > val2:
                val1, val2 = val2, val1
                
            # Use binary search to find indices, completely avoiding MemoryError from massive values
            # Rightmost val1 index gives the maximum forward reach
            curr = bisect.bisect_right(arr, val1) - 1
            idx2 = bisect.bisect_left(arr, val2)
            
            if comp[curr] != comp[idx2]:
                ans[i] = -1
                continue
                
            # If the destination is immediately reachable in 1 step
            if arr[curr] + maxDiff >= val2:
                ans[i] = 1
                continue
                
            steps = 0
            for k in range(LOG - 1, -1, -1):
                nxt = up[k][curr]
                if arr[nxt] + maxDiff < val2:
                    curr = nxt
                    steps += (1 << k)
                    
            ans[i] = steps + 2
            
        return ans