class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        i = 0
        j = 1
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
                j = j + 1
            else:
                if prices[j] - prices[i] > best:
                    best = prices[j] - prices[i]
                j = j + 1
        return best
            