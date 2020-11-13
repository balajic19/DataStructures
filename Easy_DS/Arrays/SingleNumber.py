class SingleNumber:
    def __init__(self, nums):
        self.nums = nums


    def single_number_xor(self):
        value = 0
        for each_num in self.nums:
            value ^= each_num
        return value


arr = [1, 1, 2, 2, 3, 3, 6]

print(SingleNumber(arr).single_number_xor())