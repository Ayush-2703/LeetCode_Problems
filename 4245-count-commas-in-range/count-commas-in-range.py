class Solution:
    def countCommas(self, n: int) -> int:
        count = 0

        for s in range (1, n+1):
            if s > 999:
                count+= 1
        return count  