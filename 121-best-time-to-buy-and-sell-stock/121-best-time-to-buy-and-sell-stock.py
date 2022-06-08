class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        l,r = 0,1
        for r in range(len(prices)):
            p = prices[r]-prices[l]
            mp = max(mp,p)
            if prices[r]<prices[l]:
                l=r
                r=l+1
        return mp