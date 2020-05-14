class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        profit = 0
        for i in range(length):
            if i+1 < length and prices[i+1] > prices[i]:
                temp = prices[i+1] - prices[i]
                profit += temp
        return profit