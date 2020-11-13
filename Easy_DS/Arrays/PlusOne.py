'''
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Input: digits = [9, 9]
Output: [1, 0, 0]
Explanation: The array represents the integer 123.

'''
class PlusOne:
    def __init__(self):
        return

    def plus_one_func(self, arr):
        s = ''
        dest = []
        for each_entry in arr:
            s += str(each_entry)
        s = str(int(s) + 1)
        for each_s in s:
            dest.append(int(each_s))
        return dest



arr = [9, 9]
print(PlusOne().plus_one_func(arr))
