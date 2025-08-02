from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1

if __name__ == "__main__":
    sol = Solution()
    sol.search([1, 2, 3, 4, 5], 3)
    print(sol.search([1, 2, 3, 4, 5], 3))  # output: 2