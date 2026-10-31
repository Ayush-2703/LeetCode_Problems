class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty_cells = []

        # Initialize bitmasks and collect empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty_cells.append((r, c))
                else:
                    digit = int(val)
                    mask = 1 << digit
                    box_idx = (r // 3) * 3 + (c // 3)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[box_idx] |= mask

        def backtrack(index: int) -> bool:
            if index == len(empty_cells):
                return True

            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)
            
            # Combine used digits from row, column, and 3x3 box
            used = rows[r] | cols[c] | boxes[box_idx]

            for digit in range(1, 10):
                mask = 1 << digit
                if not (used & mask):
                    # Place digit
                    board[r][c] = str(digit)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[box_idx] |= mask

                    if backtrack(index + 1):
                        return True

                    # Undo placement
                    board[r][c] = '.'
                    rows[r] &= ~mask
                    cols[c] &= ~mask
                    boxes[box_idx] &= ~mask

            return False

        backtrack(0)