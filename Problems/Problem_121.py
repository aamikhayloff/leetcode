from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if sorted(prices, reverse=True) == prices:
            return 0
        max_price, min_price = 0, prices[0]
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] < prices[i]:
                min_price = min(prices[i + 1], min_price)
            elif prices[i + 1] > prices[i]:
                max_price = prices[i + 1]
                profit = max((max_price - min_price), profit)
            else:
                continue
        return profit
