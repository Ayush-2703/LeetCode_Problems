class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        g = [0] * n
        comp = 0
        
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                comp += 1
            g[i] = comp
            
        return [g[u] == g[v] for u, v in queries]