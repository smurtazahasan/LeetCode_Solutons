class Solution:
    
    # Runtime: 437ms
    # Memory: 15.9MB
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        result = []
        
        while l <= r:
            squarel = nums[l] * nums[l]
            squarer = nums[r] * nums[r]
            
            if squarer > squarel:
                result.append(squarer)
                r -= 1
            else:
                result.append(squarel)
                l += 1
        return result[::-1]