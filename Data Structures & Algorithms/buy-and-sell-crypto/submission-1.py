class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curLow = prices[0]
        maxProf = 0
        for i in range(len(prices)):
            maxProf = max(maxProf, prices[i] - curLow)
            curLow = min(curLow, prices[i])
        
        return maxProf
