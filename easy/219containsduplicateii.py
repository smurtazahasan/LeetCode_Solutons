class Solution:
    
    # Runtime: 1375ms
    # Memory Usage: 27.5MB
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myDict = {}
        for i in range(len(nums)):
            if nums[i] in myDict and abs(i - myDict[nums[i]]) <= k:
                return True
            myDict[nums[i]] = i
        return False
    
    
    # Time Limit Exceeded
    def containsNearbyDuplicateBrute(self, nums: List[int], k: int) -> bool:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j: continue
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False