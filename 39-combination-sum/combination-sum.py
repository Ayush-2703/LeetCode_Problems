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
                # Pruning: candidates are sorted; if this exceeds remain, subsequent ones will too
                if val > remain:
                    break
                
                path.append(val)
                # Pass 'i' instead of 'i + 1' to allow reusing the same element
                backtrack(remain - val, i, path)
                path.pop()  # Backtrack
                
        backtrack(target, 0, [])
        return result