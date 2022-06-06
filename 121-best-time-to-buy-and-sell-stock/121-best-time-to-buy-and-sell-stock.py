class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0 , 1
        mp = 0
        while r < len(prices):
            p = prices[r]-prices[l]
            mp = max(mp,p)
            if prices[r]<prices[l]:
                l=r
                r=l+1
            else:
                r+=1
        return mp