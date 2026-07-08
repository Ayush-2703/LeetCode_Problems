class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:

        MOD = 10**9 + 7
        n = len(s)
        
        total = [0] * (n + 1)
        idx = [0] * (n + 1)
        pow10 = [1] * (n + 1)
        x = [0] * (n + 1)
        
        cx = 0
        ci = 0
        ct = 0
        cp = 1
        
        for i, char in enumerate(s, 1):
            d = ord(char) - 48  
            
            cp = (cp * 10) % MOD
            pow10[i] = cp
            
            ct += d
            total[i] = ct
            
            if d != 0:
                ci += 1
                cx = (cx * 10 + d) % MOD
                
            idx[i] = ci
            x[i] = cx
        
        ans = [0] * len(queries)
        
        for i, (l, r) in enumerate(queries):
            r += 1
            c = idx[r] - idx[l]
            val = (x[r] - x[l] * pow10[c]) % MOD
            ans[i] = (val * (total[r] - total[l])) % MOD
            
        return ans