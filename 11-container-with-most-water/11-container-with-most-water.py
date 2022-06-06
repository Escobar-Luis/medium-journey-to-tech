class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        res=0
        while l<r:
            w = r-l
            a = min(height[l],height[r])*w
            res = max(res,a)
            if height[l]> height[r]:
                r-=1
            else:
                l+=1
        return res