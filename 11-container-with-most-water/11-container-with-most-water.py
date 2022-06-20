class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA= 0
        l,r = 0, len(height)-1
        while l<r:
            w = r-l
            a = min(height[l],height[r]) *w
            maxA = max(a, maxA)
            if height[l]< height[r]:
                l+=1
            else: r-=1
        return maxA