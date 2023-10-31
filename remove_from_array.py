"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # check if empty
        if not nums:
            return 0

        n = len(nums)
        k = 0 # count of unique elements
        # if it is not empty
        i = 1
        # loop through array looking for duplicates
        for i in range(n):
            if nums[i] != nums[i-1] : # if they are unique
                k = k + 1
                nums[k - 1] = nums[i]

        return k
