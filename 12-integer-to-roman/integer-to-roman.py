class Solution:
    # Defining these as class-level tuples (instead of lists inside the function) 
    # completely eliminates memory allocation and garbage collection overhead on every call.
    M = ("", "M", "MM", "MMM")
    C = ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM")
    X = ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC")
    I = ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")

    def intToRoman(self, num: int) -> str:
        # f-strings are evaluated at the C-level in Python and are significantly 
        # faster than using the string concatenation (+) operator.
        return f"{self.M[num // 1000]}{self.C[(num % 1000) // 100]}{self.X[(num % 100) // 10]}{self.I[num % 10]}"