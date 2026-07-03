class Solution:
    def maxProfit(self, prices: List[int]):
        min_value=max(prices)
        max_value=0
        for i in range(len(prices)):
            if prices[i]<min_value:
                min_value=prices[i]
            else:
                diff=prices[i]-min_value
                max_value=max(diff,max_value)
        return max_value