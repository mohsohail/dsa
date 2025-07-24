from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if height[l] < height[r]:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else: 
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res


if __name__ == "__main__":
    sol = Solution()
    sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])  # Example input
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6