class Solution:
    # Runtime: 448ms
    # Memory Usage: 25.8MB
    def containsDuplicateForLoop(nums):
        myDict = {}
        for i in range(len(nums)):
            if nums[i] in myDict:
                return True
            else:
                myDict[nums[i]] = nums[i]
        return False

    # Runtime: 913ms
    # Memory Usage: 26MB
    def containsDuplicateCompareLengths(nums):
        return len(nums) != len(set(nums))

    # Runtime: 829ms
    # Memory Usage: 25.7MB
    def containsDuplicateSort(nums):
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]: return True
        return False