class IntersectionOfTwoArrays:
    def __init__(self):
        return

    def find_intersection(self, nums1, nums2):
        # Time complexity O(num1 + num2)
        # Space complexity O(min(m, n))
        if len(nums1) > len(nums2):
            return self.find_intersection(nums2, nums1)
        map = {}
        for eachNum in nums1:
            map[eachNum] = 1 + (map.get(eachNum, 0))
            # print(map.get(eachNum))
            # map.add(i, map.get(0, 1))

        intersectionList = []
        for eachNum in nums2:
            count = map.get(eachNum, 0)
            if count > 0:
                intersectionList.append(eachNum)
                map[eachNum] = count - 1

        
        return intersectionList


    def find_intersection_sort(self, num1, nums2):
        return



print(IntersectionOfTwoArrays().find_intersection([1, 2, 2, 1], [2, 2]))
# print(IntersectionOfTwoArrays().find_intersection([4, 9, 5], [9, 4, 9, 8, 4]))