class Solution:
    def gcdSum(self, nums: list[int]) -> int:

        n = len(nums)
        prefix_gcd = [0] * n
        mx = 0
        
        for i in range(n):
            if nums[i] > mx:
                mx = nums[i]
            prefix_gcd[i] = math.gcd(nums[i], mx)
            
        prefix_gcd.sort()
        
        ans = 0
        for i in range(n // 2):
            ans += math.gcd(prefix_gcd[i], prefix_gcd[n - 1 - i])
            
        return ans        