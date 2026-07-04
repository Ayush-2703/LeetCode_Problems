class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2147483647  # 2^31 - 1
        
        res = 0
        abs_x = abs(x)
        
        while abs_x != 0:
            digit = abs_x % 10
            abs_x //= 10
            
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                return 0
                
            res = res * 10 + digit
            
        return res if x >= 0 else -res