class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) -1
        area = 0
        while l<r:
            w = r-l
            a = min(height[l],height[r])*w
            area = max(area, a)
            if height[r] >= height[l]:
                l+=1
            elif height[l]>height[r]:
                r-=1
        return area        
            