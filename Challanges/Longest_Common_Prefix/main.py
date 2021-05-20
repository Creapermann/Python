"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""


from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        str_lengths = [len(x) for x in strs]
        str_lengths.sort()
        shortest_string = str_lengths[0]

        ended = False
        verified = 0

        for num in range(0, shortest_string):
            curr_char = strs[0][num]
            add_up = False
            for s in strs:
                if s[num] != curr_char:
                    add_up = False
                    ended = True
                    break

            if ended is not True:
                verified += 1

            num += 1

        a = "hello"
        b = a[:2]
        if verified == 0:
            return ""
        return strs[0][:verified]


print(Solution.longestCommonPrefix(Solution, ["cir","car"]))
