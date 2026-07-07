class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        non_zeros = [c for c in s if c != '0']
        if not non_zeros:
            return 0
            
        x = int("".join(non_zeros))
        return x * sum(int(c) for c in non_zeros)