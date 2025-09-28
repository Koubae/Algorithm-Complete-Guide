from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.soluton_1(prices)

    def soluton_1(self, prices: List[int]) -> int:
        """
        - time  O(n)
        - space O(n)
        """

        n = len(prices)

        lowest = prices[0]
        highest = -1
        profit = 0
        for price in prices[1:]:
            if price <= lowest:  # no profitable
                lowest = price
                continue

            current_profit = price - lowest
            if current_profit > profit:
                profit = current_profit

        return profit
