from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        print("strings encoded", res)
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i + length])
            i += length
        return res

if __name__ == "__main__":
    solution = Solution()
    encoded = solution.encode(["hello", "world"])
    print(f"Encoded: {encoded}")
    decoded = solution.decode(encoded)
    print(f"Decoded: {decoded}")

# time complexity: O(n)
# space complexity: O(n)