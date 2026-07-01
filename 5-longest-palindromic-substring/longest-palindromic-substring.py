class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        p = [0] * n
        center = right = 0
        
        for i in range(1, n - 1):
            mirror = 2 * center - i
            
            if right > i:
                p[i] = min(right - i, p[mirror])
                
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1
                
            if i + p[i] > right:
                center, right = i, i + p[i]
                
        max_len, max_center = max((val, idx) for idx, val in enumerate(p))
        
        start = (max_center - max_len) // 2
        return s[start:start + max_len]