"""
Challange:

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
"""

class Solution:
    def maxScore(self, s: str) -> int:
        return max(list(s[:n + 1].count("0") + s[:-len(s)+n:-1].count("1")  for n in range(0, len(s) - 1)))

print(Solution.maxScore(Solution, "1111"))