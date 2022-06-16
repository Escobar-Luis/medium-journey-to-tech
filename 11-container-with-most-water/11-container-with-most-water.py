class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height) -1
        m = 0
        while l<r:
            w = r-l
            a = min(height[l], height[r]) * w
            m = max(m, a)
            if height[l]< height[r]:
                l+=1
            else:
                r-=1
        return m
        