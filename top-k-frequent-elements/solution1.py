from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        print(f"Element frequencies: {count}")

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
            print(f"Current result: {res}")

if __name__ == "__main__":
    solution = Solution()
    result = solution.topKFrequent([1, 1, 1, 1, 1, 2, 2, 2, 3], 2)
    print(f"Top K Frequent Elements: {result}")  


# time complexity: O(nlogn)
# space complexity: O(n)