from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            res = max(res, area)
        return res


if __name__ == "__main__":
    sol = Solution()
    sol.maxArea([1,8,6,2,5,4,8,3,7])
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49