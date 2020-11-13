# Code to return True if a duplice is found in the array/list
class FindDuplicates:
    def __init__(self, nums):
        self.nums = nums

    def duplicate_using_sort(self):
        '''
        Time Complexity: O(nlogn)
        Space Complexity: O(1)
        '''
        self.nums.sort()

        for i in range(len(self.nums) - 1):
            if self.nums[i] == self.nums[i+1]:
                return True

        return False


    def duplicate_using_set(self):
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        numsLen = len(self.nums)
        setNumsLen = len(set(self.nums))
        if numsLen != setNumsLen:
            return True

        return False


    def duplicate_using_hashmap(self):
        '''
        Time Complexity: O(nlogn)
        Space Complexity: O(1)

        Works only if the numbers in array are less than length of the array
        EG: [1, 2, 3, 3, 4, 5, 5]
        '''
        numsLen = len(self.nums)
        for i in range(numsLen):
            self.nums[self.nums[i] % numsLen] = self.nums[self.nums[i] % numsLen] + numsLen

        for i in range(numsLen):
            if (self.nums[i] > numsLen *2):
                return True
        return False

arr = [1, 1, 2, 0, 0]
print(FindDuplicates(arr).duplicate_using_sort())
# print(FindDuplicates(arr).duplicate_using_set())
# print(FindDuplicates(arr).duplicate_using_hashmap())
