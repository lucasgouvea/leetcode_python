from typing import List


class Solution121:
    def max_profit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        
        while r < len(prices):
            sell = prices[r]
            buy = prices[l]
            profit = sell - buy
            if profit > 0:
                if profit > max_profit:
                    max_profit = profit
            else:
                l = r
            r += 1

        return max_profit
