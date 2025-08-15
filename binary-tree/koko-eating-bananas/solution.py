import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2

            hours_needed = sum(math.ceil(pile / mid) for pile in piles)
            if hours_needed <= h:
                r = mid - 1
            else:
                l = mid + 1
        return l


if __name__ == "__main__":
    sol = Solution()
    print(sol.minEatingSpeed([3, 6, 7, 11], 8))  # Example usage
    print(sol.minEatingSpeed([30, 11, 23, 4, 20], 5))  # Example usage
    print(sol.minEatingSpeed([30, 11, 23, 4, 20], 6))  # Example usage