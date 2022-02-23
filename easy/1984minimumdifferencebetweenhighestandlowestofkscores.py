class Solution:
    
    # Runtime: 284ms
    # Memory Usage: 14.2MB
    
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l, r = 0, k - 1
        result = float('inf')
        nums.sort()
        
        while r < len(nums):
            Large = max(nums[l:r+1])
            Min = min(nums[l:r+1])
            score = abs(Large - Min)
            result = min(score, result)
            l, r = l + 1, r + 1
            
        return result