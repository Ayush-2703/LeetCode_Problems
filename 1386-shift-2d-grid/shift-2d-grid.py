class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid[0])
        total = len(grid) * n
        k %= total
        
        if k == 0:
            return grid
            
        flat = [val for row in grid for val in row]
        
        flat = flat[-k:] + flat[:-k]
        
        return [flat[i : i + n] for i in range(0, total, n)]       