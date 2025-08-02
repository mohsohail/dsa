from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1

        while l <= r:
            mid = (l + r) // 2
            row = mid // cols
            col = mid % cols
            mid_value = matrix[row][col]

            if mid_value < target:
                l = mid + 1
            elif mid_value > target:
                r = mid - 1
            else:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    sol.searchMatrix([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 9)
    print(sol.searchMatrix([[1, 3, 5], [7, 9, 11], [13, 15, 17]], 9))  # Output: True