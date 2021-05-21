"""
Challange:

Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.
A word is a maximal substring consisting of non-space characters only.
"""



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        spliced = s.split(' ')
        spliced = [x for x in spliced if x != '']
        if len(spliced) >= 1:
            return len(spliced[-1])
        else:
            return 0



print(Solution.lengthOfLastWord(Solution, "Hello World"))