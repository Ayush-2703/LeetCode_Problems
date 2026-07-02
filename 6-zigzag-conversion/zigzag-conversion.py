class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
            
        res = []
        cycle_len = 2 * numRows - 2
        n = len(s)
        
        for i in range(numRows):
            for j in range(0, n - i, cycle_len):
                res.append(s[j + i])
                if i != 0 and i != numRows - 1 and j + cycle_len - i < n:
                    res.append(s[j + cycle_len - i])
                    
        return "".join(res)