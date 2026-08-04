class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        
        num_set = set(nums)
        min_val = min(nums)
        max_val = max(nums)
        
        return [x for x in range(min_val, max_val + 1) if x not in num_set]