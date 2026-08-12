from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            # Expand window
            freq[nums[right]] += 1
            
            # Shrink window if any element's frequency exceeds k
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            
            # Update answer
            max_len = max(max_len, right - left + 1)
            
        return max_len