from typing import List

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        
        res = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i != j:
                    prod *= nums[j]
            res.append(prod)
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
