class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:

        MOD = 10**9 + 7
        dp = {(0, 0): 1}
        
        for x in nums:
            new_dp = dp.copy()
            for (g1, g2), cnt in dp.items():
                # Add current element to the first subsequence
                ng1 = math.gcd(g1, x)
                new_dp[(ng1, g2)] = (new_dp.get((ng1, g2), 0) + cnt) % MOD
                
                # Add current element to the second subsequence
                ng2 = math.gcd(g2, x)
                new_dp[(g1, ng2)] = (new_dp.get((g1, ng2), 0) + cnt) % MOD
                
            dp = new_dp
            
        ans = sum(cnt for (g1, g2), cnt in dp.items() if g1 == g2 and g1 > 0)
        return ans % MOD        