class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        profit = 0
        max_profit = 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            if prices[right] < prices[left]:
                left = right

            max_profit = max(max_profit, profit)
            right += 1

        return max_profit