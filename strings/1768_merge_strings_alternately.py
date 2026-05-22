# Problem: Merge Strings Alternately
# LeetCode #: 1768
# Difficulty: Easy
# Topic: strings / two pointers
# URL: https://leetcode.com/problems/merge-strings-alternately/
#
# Problem:
#   Given two strings word1 and word2, merge them by adding letters in
#   alternating order starting with word1. If one string is longer, append
#   the remaining letters at the end.
#
# Examples:
#   Input:  word1 = "abc", word2 = "pqr"  -> Output: "apbqcr"
#   Input:  word1 = "ab",  word2 = "pqrs" -> Output: "apbqrs"
#   Input:  word1 = "abcd",word2 = "pq"   -> Output: "apbqcd"
#
# Constraints:
#   - 1 <= word1.length, word2.length <= 100
#   - word1 and word2 consist of lowercase English letters
#
# Approach:
#   zip() pairs characters up to the shorter string's length.
#   Slicing from the other string's length captures the leftover tail.
#   One of the two tail slices will always be an empty string.
#
# Time:  O(n + m)  — n, m are lengths of word1, word2
# Space: O(n + m)  — for the result string


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        paired = "".join(a + b for a, b in zip(word1, word2))
        return paired + word1[len(word2):] + word2[len(word1):]


# --- Roger's original solution (for reference) ---
class SolutionOriginal:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = []
        merge2 = []
        if len(word1) == len(word2):
            for i in range(len(word1)):
                merge.append(word1[i])
                merge.append(word2[i])
                merge2 = "".join(merge)
            return merge2
        elif len(word1) > len(word2):
            for i in range(len(word2)):
                merge.append(word1[i])
                merge.append(word2[i])
            for j in range(len(word2), len(word1), 1):
                merge.append(word1[j])
                merge2 = "".join(merge)
            return merge2
        elif len(word1) < len(word2):
            for i in range(len(word1)):
                merge.append(word1[i])
                merge.append(word2[i])
            for j in range(len(word1), len(word2), 1):
                merge.append(word2[j])
                merge2 = "".join(merge)
            return merge2


# --- Tests ---
if __name__ == "__main__":
    s = Solution()
    assert s.mergeAlternately("abc", "pqr") == "apbqcr"
    assert s.mergeAlternately("ab", "pqrs") == "apbqrs"
    assert s.mergeAlternately("abcd", "pq") == "apbqcd"
    assert s.mergeAlternately("a", "b") == "ab"
    assert s.mergeAlternately("a", "bcd") == "abcd"
    print("All tests passed.")
