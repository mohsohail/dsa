from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(f"Comparing '{s}' and '{t}'")

        if len(s) != len(t):
            return False
        
        count_s = Counter(s)
        count_t = Counter(t)

        if count_s == count_t:
            print("The strings are anagrams.")
            return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))  # Output: True