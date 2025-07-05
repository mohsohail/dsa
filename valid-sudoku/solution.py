from typing import List
from collections import defaultdict

class Solution:
    def valid_sudoku(self, board: List[List[str]]) -> bool:
        print("Checking if the board is a valid Sudoku...")
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)


        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                if num in rows[r] or num in cols[c] or num in squares[(r // 3, c // 3)]:
                    print(f"Duplicate found: {num} at row {r}, column {c}")
                    return False
                rows[r].add(num)
                cols[c].add(num)
                squares[(r // 3, c // 3)].add(num)
        return True

if __name__ == "__main__":
    solution = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "1", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", "6", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(solution.valid_sudoku(board))  # Output: True