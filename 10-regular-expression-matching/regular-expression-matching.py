class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)

        def matches(si: int, pj: int) -> bool:
            return p[pj] == '.' or p[pj] == s[si]

        prev = [False] * (n + 1)
        prev[0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 2]

        for i in range(1, m + 1):
            curr = [False] * (n + 1)
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    curr[j] = curr[j - 2] or (matches(i - 1, j - 2) and prev[j])
                else:
                    curr[j] = matches(i - 1, j - 1) and prev[j - 1]
            prev = curr

        return prev[n]        