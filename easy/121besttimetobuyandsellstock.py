class Solution:
    
    # Runtime: 1452ms
    # Space: 25.1MB
    def maxProfitKadane(self, prices: List[int]) -> int:
        currMin, currBestPrice = float("inf"), 0
        for i in range(len(prices)):
            currMin = min(currMin, prices[i])
            currBestPrice = max(currBestPrice, prices[i] - currMin)
        return currBestPrice
            
      
    def maxProfitNested(prices):
        currMax = -float("inf")
        buyIndex, sellIndex = 0, 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if i == j: continue
                if prices[j] - prices[i] > currMax:
                    currMax, buyIndex, sellIndex = prices[j] - prices[i], i, j
        
        if currMax > 0: return currMax
        else: return 0 
        