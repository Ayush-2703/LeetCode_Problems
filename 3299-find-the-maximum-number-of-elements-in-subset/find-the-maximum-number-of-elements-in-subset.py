class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 1
        
        if 1 in count:
            c = count[1]
            ans = max(ans, c if c % 2 != 0 else c - 1)
            
        for x in count:
            if x == 1:
                continue
            
            curr = x
            sz = 0
            
            while count[curr] >= 2 and (curr * curr) in count:
                sz += 2
                curr *= curr
            
            sz += 1
            ans = max(ans, sz)
            
        return ans