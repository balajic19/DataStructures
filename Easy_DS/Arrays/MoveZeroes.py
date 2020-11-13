'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class MoveZeroes:
    def __init__(self):
        return
    
    def move_zeros_func(self, arr):
        flag = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[flag] = arr[i]
                flag += 1
        while(flag < len(arr)):
            arr[flag] = 0
            flag += 1
        return arr


arr = [1, 0, 2, 0, 3]
print(MoveZeroes().move_zeros_func(arr))