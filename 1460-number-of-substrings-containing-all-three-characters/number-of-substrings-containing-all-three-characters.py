class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        ans = 0
        
        for i, char in enumerate(s):
            last_seen[char] = i
            ans += min(last_seen['a'], last_seen['b'], last_seen['c']) + 1
            
        return ans