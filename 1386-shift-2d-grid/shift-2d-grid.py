class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid[0])
        total = len(grid) * n
        k %= total
        
        if k == 0:
            return grid
            
        # Flattening via list comprehension is highly optimized in CPython
        flat = [val for row in grid for val in row]
        
        # Slicing shifts the elements efficiently at the C-level
        flat = flat[-k:] + flat[:-k]
        
        # Rebuilding the 2D array using step slicing
        return [flat[i : i + n] for i in range(0, total, n)]       