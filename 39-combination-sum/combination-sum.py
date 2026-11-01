class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        
        def backtrack(remain: int, start: int, path: list[int]):
            if remain == 0:
                result.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                val = candidates[i]
                if val > remain:
                    break
                
                path.append(val)
                backtrack(remain - val, i, path)
                path.pop()  
                
        backtrack(target, 0, [])
        return result