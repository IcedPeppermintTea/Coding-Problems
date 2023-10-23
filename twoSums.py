"""
Given an array of integers nums 
and an integer target, return indices 
of the two numbers such that they add up to target.
"""

class NumSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            firstnum = nums[i]
            firstnumidx = i
            nextnum = nums[i+1]
            nextnumidx = i+1
            addition = firstnum + nextnum
            if (addition == target):
                return [firstnumidx, nextnumidx]
            else:
                i = i + 1
        
