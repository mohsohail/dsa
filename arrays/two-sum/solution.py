from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for numKey, numVal in enumerate(nums):
            diff = target - numVal
            if diff in seen:
                return [seen[diff], numKey]
            seen[numVal] = numKey

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]