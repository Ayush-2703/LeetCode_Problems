class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:

        M = max(nums)
        freq = [0] * (M + 1)
        
        for x in nums:
            freq[x] += 1
            
        exact = [0] * (M + 1)
        
        # Traverse backwards to compute exact GCD frequencies using inclusion-exclusion
        for i in range(M, 0, -1):
            c = 0
            # Count how many numbers are multiples of i
            for j in range(i, M + 1, i):
                c += freq[j]
            
            # Total pairs where both numbers are multiples of i
            pairs = c * (c - 1) // 2
            
            # Subtract pairs where the GCD is a STRICT multiple of i (like 2i, 3i, etc.)
            for j in range(2 * i, M + 1, i):
                pairs -= exact[j]
                
            exact[i] = pairs
            
        # Build prefix sums to identify the ranges of each GCD in the sorted array
        prefix = [0] * (M + 1)
        for i in range(1, M + 1):
            prefix[i] = prefix[i - 1] + exact[i]
            
        # Binary search the queries over the prefix sums for O(log M) O(1) lookups
        return [bisect.bisect_right(prefix, q) for q in queries]        