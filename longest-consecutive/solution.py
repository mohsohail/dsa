from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1

                while (num + length) in numSet:
                    length += 1
                    longest = max(length, longest)
        return longest

if __name__ == "__main__":
    solution = Solution()
    solution.longestConsecutive([100, 4, 200, 1, 3, 2])
