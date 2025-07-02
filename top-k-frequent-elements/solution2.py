from typing import List
from collections import Counter
from heapq import nlargest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = nlargest(k, count.keys(), key=lambda x: count[x])
        return res

if __name__ == "__main__":
    solution = Solution()
    result = solution.topKFrequent([1, 1, 1, 1, 1, 2, 2, 2, 3], 2)
    print(f"Top K Frequent Elements: {result}")  


# time complexity: O(nlogn)
# space complexity: O(n)
        