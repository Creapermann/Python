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