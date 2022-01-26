class Solution:

    # Runtime: 378ms
    # Space: 23.1MB
    def findDisappearedNumbersDictionary(nums):
        myDict, result = {}, []
        for i in range(len(nums)):
                myDict[nums[i]] = nums[i]
        for i in range(1, len(nums)+1):
                if i not in myDict: result.append(i)
        return result

    # Runtime: 723ms
    # Space: 41.8MB
    def findDisappearedNumbersNumPy(nums):
        import numpy as np
        numlist = set(np.arange(1, len(nums)+1))
        return list(numlist - set(nums))

    # Runtime: 404ms
    # Space: 25.2MB
    def findDisappearedNumbersSet(nums):
        numlist = []
        for i in range(1, len(nums)+1):
                numlist.append(i)
        return list(set(numlist) - set(nums))