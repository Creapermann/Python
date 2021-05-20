"""
Challange:

Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
"""

class Solution:
    def check(self, nums) -> bool:

        # check if already sorted
        if nums == sorted(nums):
            return True

        # get the index where the old (already sorted) array was spliced and swapped
        n = 0
        while True:
            if nums[n] > nums[n+1]:
                break
            n += 1

        # sepperate the list into the old parts at the swap index
        list_one = nums[:n+1]
        list_two = nums[n+1:]
        # put the lists back in the original form and see if its sorted
        sorted_list = list_two + list_one

        return sorted_list == sorted(sorted_list)




print(Solution.check(Solution, [2,1]))