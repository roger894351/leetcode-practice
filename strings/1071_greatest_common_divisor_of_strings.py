# Problem: Greatest Common Divisor of Strings
# LeetCode #: 1071
# Difficulty: Easy
# Topic: strings / math
# URL: https://leetcode.com/problems/greatest-common-divisor-of-strings/
#
# Problem:
#   "t divides s" means s = t + t + ... + t (t concatenated one or more times).
#   Given str1 and str2, return the largest string x that divides both.
#
# Examples:
#   "ABCABC", "ABC"   -> "ABC"
#   "ABABAB", "ABAB"  -> "AB"
#   "LEET",   "CODE"  -> ""
#   "AAAAAB", "AAA"   -> ""
#
# Constraints:
#   - 1 <= str1.length, str2.length <= 1000
#   - str1 and str2 consist of uppercase English letters


# ── Approach 1: Brute Force ────────────────────────────────────────────────
#
# The GCD string must be a prefix of both str1 and str2, AND its length must
# divide both lengths evenly.  Try every prefix length from largest to smallest.
#
# Time:  O(min(n,m) * (n+m))  — each check costs O(n+m) for string comparison
# Space: O(n+m)

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def divides(s: str, t: str) -> bool:
            """Return True if t divides s (s = t repeated k times)."""
            if len(s) % len(t) != 0:          # length must divide evenly
                return False
            return t * (len(s) // len(t)) == s # verify by rebuilding s

        # try every prefix length from largest to smallest
        for length in range(min(len(str1), len(str2)), 0, -1):
            candidate = str1[:length]
            if divides(str1, candidate) and divides(str2, candidate):
                return candidate

        return ""


# ── Approach 2: Math — GCD of lengths (optimal) ───────────────────────────
#
# Key insight:
#   If a string x divides both str1 and str2, then:
#       str1 + str2  ==  str2 + str1
#   (both sides equal x repeated (len(str1)/len(x) + len(str2)/len(x)) times)
#
#   If that condition holds, the answer length is gcd(len(str1), len(str2)).
#   We can prove no longer divisor is possible because any common divisor's
#   length must divide both lengths — so the maximum is their gcd.
#
# Time:  O(n + m)   — one string concatenation check + O(log min(n,m)) for gcd
# Space: O(n + m)   — for the concatenated strings

from math import gcd

class SolutionMath:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If no common divisor exists at all, concatenation order matters
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]


# ── Roger's Original Attempt (for reference) ──────────────────────────────
# Issue: finds common prefix chars only — does not verify repetition
# Also: len(unit)/2 result is discarded; / gives float in Python 3 (use //)
class SolutionOriginal:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        unit = []
        for i in range(len(str2)):
            if i == 0 and str2[0] == str1[0]:
                unit.append(str2[i])
            if i != 0 and str2[i] == str1[i]:
                unit.append(str2[i])
            else:
                pass
        len(unit) / 2  # BUG: result discarded; also float division
        for j in range(len(unit) // 2):  # would crash with / in Python 3
            if unit[j] == unit[2 * (j + 1) - 1]:
                unit = unit[:j]
        largest_unit = ''.join(unit)
        # Missing: never returned, never verified against str1/str2


# ── Tests ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    for Sol in (Solution, SolutionMath):
        s = Sol()
        assert s.gcdOfStrings("ABCABC", "ABC")  == "ABC"
        assert s.gcdOfStrings("ABABAB", "ABAB") == "AB"
        assert s.gcdOfStrings("LEET",   "CODE") == ""
        assert s.gcdOfStrings("AAAAAB", "AAA")  == ""
        assert s.gcdOfStrings("A",      "A")    == "A"
        assert s.gcdOfStrings("AA",     "A")    == "A"

    print("All tests passed.")
