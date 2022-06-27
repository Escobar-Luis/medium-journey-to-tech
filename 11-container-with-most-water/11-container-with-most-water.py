class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0, len(height)-1
        while l<r:
            w = r-l
            a = w * min(height[l],height[r])
            res = max(a, res)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return res