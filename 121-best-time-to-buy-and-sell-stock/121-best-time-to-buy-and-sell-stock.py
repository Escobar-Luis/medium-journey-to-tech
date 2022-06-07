class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l,r = 0,1
        while r < len(prices):
            p = prices[r]-prices[l]
            res = max(res, p)
            if prices[r]<prices[l]:
                l=r
                r= l+1
            else:
                r+=1
        return res