'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class TwoSum:
    def __init__(self):
        return

    def tow_sum_func(self, nums, target):
        map = {}
        for i in range(len(nums)):
            complement = abs(target - nums[i])
            if complement in map:
                return [nums.index(complement), i]
            map[nums[i]] = True
        return []


arr = [1, 2, 6, 9]
target = 10


print(TwoSum().tow_sum_func(arr, target))