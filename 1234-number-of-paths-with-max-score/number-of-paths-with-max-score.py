class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        prev_row = [(-1, 0)] * n

        for i in range(n - 1, -1, -1):
            curr_row = [(-1, 0)] * n
            for j in range(n - 1, -1, -1):
                ch = board[i][j]

                if ch == 'X':
                    continue 
                if ch == 'S':
                    curr_row[j] = (0, 1)
                    continue

                best_sum, best_cnt = -1, 0
                for s, c in (
                    prev_row[j],                                   
                    curr_row[j + 1] if j + 1 < n else (-1, 0),      
                    prev_row[j + 1] if j + 1 < n else (-1, 0),      
                ):
                    if s == -1:
                        continue
                    if s > best_sum:
                        best_sum, best_cnt = s, c
                    elif s == best_sum:
                        best_cnt += c

                if best_sum != -1:
                    val = 0 if ch == 'E' else int(ch)
                    curr_row[j] = (best_sum + val, best_cnt % MOD)

            prev_row = curr_row

        max_sum, ways = prev_row[0]
        return [0, 0] if max_sum == -1 else [max_sum, ways]        