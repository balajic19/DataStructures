
class RemoveDuplicatesArray:
    def __init__(self):
        return 

    def remove_duplicates(self, nums):
        # Time complexity is O(n)
        numLength = len(nums)
        if numLength == 0 or numLength == 1:
            return numLength

        i = 0
        for j in range(numLength-1):
            if nums[j] != nums[j+1]:
                nums[i] = nums[j]
                i += 1

        nums[i] = nums[numLength - 1]
        return nums[:i+1]

    def remove_duplicates_hashmap(self, nums):
        # Time Complexity is O(m + n) where m is size of map
        map ={}
        for eachNum in nums:
            map[eachNum] = map.get(eachNum, 0) + 1

        return list(map.keys())



# nums = [5, 5, 4, 6, 7, 3, 1, 6, 1, 3]
nums = [5, 4, 3, 3, 3, 2, 1, 1]
a = RemoveDuplicatesArray()

print(a.remove_duplicates(nums)) # REMOVES DUPLICATES FROM A SORTED ARRAY ONLY
# print(a.remove_duplicates_hashmap(nums))

