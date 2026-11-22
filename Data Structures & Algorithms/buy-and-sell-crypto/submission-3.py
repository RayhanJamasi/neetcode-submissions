class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        max_value = 0
        curr = 0
        left = 0
        right = left + 1

        for right in range(len(prices)):
            if prices[left] < prices[right]:
                curr = prices[right] - prices[left]
                
                #getting max
                if (curr > max_value):
                    max_value = curr
                
            else:
                left = right

        return max_value

        