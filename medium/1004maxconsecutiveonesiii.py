class Solution:
    
    # Runtime: 809ms
    # Memory Usage: 14.8MB
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, curr, maxLength = 0, 0, -float('inf')
        
        for r in range(len(nums)):
            
            # If next is 1, then we can add to counter
            if nums[r]: curr += 1
            
            
            # If we exceed our K limit, then shrink
            if (r - l + 1) - curr > k:
                if nums[l]: curr -= 1
                l += 1
            
            # Store max value
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength