class Solution:
    def sumAndMultiply(self, n: int) -> int:
        rev_x = 0
        digit_sum = 0
        temp = n
        while temp > 0:
            d = temp % 10
            if d != 0:
                rev_x = rev_x * 10 + d
                digit_sum += d
            temp //= 10

        x = 0
        while rev_x > 0:
            x = x * 10 + rev_x % 10
            rev_x //= 10

        return x * digit_sum