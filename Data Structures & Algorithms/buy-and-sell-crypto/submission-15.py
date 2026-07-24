class Solution:
    def maxProfit(self, prices: List[int]):
        min_val=max(prices)
        max_profit=0

        for i in range(len(prices)):
            if prices[i]<min_val:
                min_val=prices[i]

            else:
                diff=prices[i]-min_val
                max_profit=max(diff,max_profit)

        return max_profit