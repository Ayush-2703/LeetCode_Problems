class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            a = sorted(s)
            b = sorted(t)
            if a == b:
                return True
            else:
                return False
        else:
            return False