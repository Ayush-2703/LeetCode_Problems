class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        unique=set(s)
        for char in unique:
            if s.count(char)!=t.count(char):
                return False
        return True