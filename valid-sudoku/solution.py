from typing import List

class Solution:
    def valid_sudoku(self, board: List[List[str]]) -> bool:
        print("Checking if the board is a valid Sudoku...")
        rows, cols, boxes = set(), set(), set()

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue

                if (r, num) in rows or (num, c) in cols or (r // 3, c // 3, num) in boxes:
                    print(f"Invalid number {num} found at row {r}, column {c}.")
                    return False
                
                rows.add((r, num))
                cols.add((num, c))
                boxes.add((r // 3, c // 3, num))
        print("The board is a valid Sudoku.")
        return True

if __name__ == "__main__":
    solution = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "5", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", "6", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(solution.valid_sudoku(board))  # Output: True