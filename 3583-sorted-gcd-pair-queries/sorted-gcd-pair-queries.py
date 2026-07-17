class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:

        M = max(nums)
        freq = [0] * (M + 1)
        
        for x in nums:
            freq[x] += 1
            
        exact = [0] * (M + 1)
        
        for i in range(M, 0, -1):
            c = 0
            for j in range(i, M + 1, i):
                c += freq[j]
           
            pairs = c * (c - 1) // 2
            
            for j in range(2 * i, M + 1, i):
                pairs -= exact[j]
                
            exact[i] = pairs
        
        prefix = [0] * (M + 1)
        for i in range(1, M + 1):
            prefix[i] = prefix[i - 1] + exact[i]
        
        return [bisect.bisect_right(prefix, q) for q in queries]        