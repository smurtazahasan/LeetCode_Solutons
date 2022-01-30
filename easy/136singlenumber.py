class Solution:
    
    # Run Time: 317ms
    # Space: 16.8MB
    def singleNumber(self, nums: List[int]) -> int:
        myDict = {}
        for i in nums:
            myDict[i] = 2 if i in myDict else 1
        for i in myDict:
            if myDict[i] == 1: return i
    
    # Run Time: 273ms
    # Space: 16.7MB
    def singleNumberXOR(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1, len(nums)):
            result = result ^ nums[i]
        return result