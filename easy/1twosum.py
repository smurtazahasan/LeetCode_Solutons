class Solution:
    
    # Run Time: 57ms
    # Space: 15.3MB
    def twoSumDict(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i in range(len(nums)):
            if target - nums[i] in myDict: 
                return [i, myDict[target - nums[i]]]
            else:
                myDict[nums[i]] = i
                
                
    # Run Time: 4540ms
    # Space: 15MB            
    def twoSumBrute(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j: continue
                if nums[i] + nums[j] == target:
                    return [i, j]