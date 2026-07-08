class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:

        MOD = 10**9 + 7
        n = len(s)
        
        pow10 = [1] * (n + 1)
        idx = [0] * (n + 1)
        x = [0] * (n + 1)
        total = [0] * (n + 1)
        
        for i in range(n):
            d = int(s[i])
            pow10[i+1] = (pow10[i] * 10) % MOD
            
            if d != 0:
                idx[i+1] = idx[i] + 1
                x[i+1] = (x[i] * 10 + d) % MOD
            else:
                idx[i+1] = idx[i]
                x[i+1] = x[i]
                
            total[i+1] = total[i] + d
            
        ans = []
        for l, r in queries:
            count = idx[r+1] - idx[l]
            val = (x[r+1] - x[l] * pow10[count]) % MOD
            digit_sum = total[r+1] - total[l]
            
            ans.append((val * digit_sum) % MOD)
            
        return ans        