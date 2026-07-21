class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        z = [len(x) for x in s.split('1') if x]
        
        max_gain = max([z[i] + z[i+1] for i in range(len(z) - 1)], default=0)
        
        return s.count('1') + max_gain        