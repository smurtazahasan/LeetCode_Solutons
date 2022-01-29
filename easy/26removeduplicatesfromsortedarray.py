class Solution:
    
    # Run Time: 93ms
    # Space: 15.7MB
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]:
                nums[curr] = nums[i+1]
                curr += 1
        return curr
    
    
    # Run Time: 292ms
    # Space: 15.6MB
    def removeDuplicatesSimple(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        a, b = 0, 1
        while b != len(nums):
            if nums[a] == nums[b]:
                del nums[b]
            else:
                a, b = a + 1, b + 1
        return len(nums)