class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #list반복, target의 수가 더 적어지면 change
        target = prices[0]
        result = 0
        for price in prices:
            # target 변경
            if price < target:
                target = price
            if price - target > 0:
                result = max(result, price - target)
        return result
