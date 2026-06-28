class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        counts = [0] * (n + 1)
        
        for num in arr:
            counts[min(num, n)] += 1
            
        ans = 0
        for i in range(1, n + 1):
            ans = min(ans + counts[i], i)
            
        return ans