class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float('inf')
        maxi = float('-inf')

        for i in range(len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            maxi = max(maxi, prices[i] - mini)

        return maxi