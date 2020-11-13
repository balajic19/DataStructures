class RotateArrayLeft:
    def __init__(self):
        return 

    def rotate_using_slicing(self, nums, k):
        k %= len(nums)
        # code that movesright
        # nums[k:], nums[:k] = nums[:-k], nums[-k:]
        nums[:-k], nums[-k:] = nums[k:], nums[:k]
        # nums[-k:], nums[:-k] = nums[:k], nums[k:]
        return nums

    def rotate_using_reverse_algo(self, nums, k):
        numsLen = len(nums)
        k %= numsLen

        self.rotate(numsLen-1, numsLen-k, nums)
        self.rotate(numsLen-k-1, 0, nums)
        self.rotate(numsLen-1, 0, nums)
        return nums

    def rotate(self, start, end, arr):
        while(start > end):
            temp = arr[end]
            arr[end] = arr[start]
            arr[start] = temp

            start -= 1
            end += 1



arr = [1, 2, 3, 4, 5]
k = 1
obj = RotateArrayLeft()

print(obj.rotate_using_slicing(arr, k))