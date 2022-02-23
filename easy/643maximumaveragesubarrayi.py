class Solution:
    
    # Runtime: 1332ms
    # Memory Usage: 26.3MB
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum, maxAverage, l = 0, -float('inf'), 0
        
        for r in range(len(nums)):
            currSum += nums[r]
            if r >= k - 1:
                maxAverage = max(maxAverage, currSum/(r - l + 1))
                currSum -= nums[l]
                l += 1
        return maxAverage
    
    
    
    # Time Limit Exceeded
    def findMaxAverageMethod1(self, nums: List[int], k: int) -> float:
        maxAverage = -float('inf')
        l, r = 0, k - 1
        
        while r < len(nums):
            maxAverage = max(maxAverage, sum(nums[l:r + 1])/(r - l + 1))
            l, r = l + 1, r + 1
        return maxAverage