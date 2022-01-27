class Solution:

    # Runtime: 211ms
    # Space: 15.9MB
    def missingNumberDictionary(nums):
        myDict = {}
        for i in nums:
            myDict[i] = i
        for i in range(len(nums) + 1):
            if i not in myDict:
                return i


    # Runtime: 213ms
    # Space: 15.4MB
    def missingNumberForLoop(nums):
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i != nums[i]:
                return i
        return n


    # Runtime: 294ms
    # Space: 15.5MB
    def missingNumberSum(nums):
        return (len(nums)*(len(nums)+1))//2 - sum(nums)


    # Runtime: 160ms
    # Space: 15.4MB 
    def missingNumberXOR(nums):
        result = 0
        # Get XOR Val of numbers of expected list
        for i in range(len(nums)+1):
            result = result ^ i
        print("OG XOR Value is: ", result, " from 0 to ", len(nums)+1)

        #Get XOR Val of given list
        for i in nums:
            result = result ^ i
        return result


    # Runtime: 190ms
    # Space: 15.4MB
    def missingNumberZip(nums):
        nums.sort()
        numList = []
        for i in range(len(nums)+1):
            numList.append(i)
        nums.append(0)
        for a, b in zip(numList, nums):
            if a == b: continue
            else: return a
