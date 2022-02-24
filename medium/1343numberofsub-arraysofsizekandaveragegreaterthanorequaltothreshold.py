class Solution:
    
    # Run Time: 903ms
    # Space: 27.3MB
    
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, result = 0, 0
        currSum = 0
        
        for r in range(len(arr)):
            currSum += arr[r]
            
            if r >= k - 1:
                if currSum/k >= threshold: result += 1
                currSum -= arr[l]
                l += 1
            
        return result