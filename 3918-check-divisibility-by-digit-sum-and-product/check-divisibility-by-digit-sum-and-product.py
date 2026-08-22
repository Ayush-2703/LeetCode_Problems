class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digitSum = 0
        digitProduct = 1
        Original = n

        while n > 0:
            digit = n % 10
            n //= 10

            digitSum += digit
            digitProduct *= digit

        return Original % (digitSum + digitProduct) == 0