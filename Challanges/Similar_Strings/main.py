"""
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose 
two indices in a string (not necessarily different) and swap the characters at these indices.
Return true if it is possible to make both strings equal by performing at most one string swap 
on exactly one of the strings. Otherwise, return false.
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """ Checking if only 2 chars in the strings are different """

        # Check if the string contains the same letters (it needs to)
        if set(s1) != set(s2):
            return False

        n, diff_chars = 0, 0
        while n != len(s1):
            if s1[n] != s2[n]:
                diff_chars += 1
            n += 1

        return diff_chars == 2 or diff_chars == 0


print(Solution.areAlmostEqual(Solution, "caa", "aaz"))
