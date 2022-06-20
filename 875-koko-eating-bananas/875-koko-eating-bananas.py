class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        
        k = 0
        
        while l<=r:
            m = (l+r) //2
            hours = 0
            for p in piles:
                hours += math.ceil(p/m)
            if hours > h:
                l = m +1
            else:
                k = m
                r = m-1
        return k