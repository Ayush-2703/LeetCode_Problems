class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def get_digit_product(num: int) -> int:
            prod = 1
            while num > 0:
                prod *= num % 10
                num //= 10
            return prod

        for current in range(n, n + 10):
            if get_digit_product(current) % t == 0:
                return current