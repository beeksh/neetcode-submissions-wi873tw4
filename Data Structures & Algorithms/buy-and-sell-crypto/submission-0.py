class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        m = prices[-1]
        for price in prices[len(prices)-1::-1]:
            if price>m:
                m = price
                continue
            else:
                if m-price>maxp:
                    maxp = m-price
        return maxp