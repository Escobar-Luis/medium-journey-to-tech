from typing import List

def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        
        # they can never equal each other because we need distance from them
        while l < r:
            # Max between largest area seen, the minimum value between the left and right pointer multiplied by the distance or length between them
            res = max(res, min(height[l], height[r]) * (r - l))
            # if our left pointer is less than our right pointer, increment the left
            if height[l] < height[r]:
                l += 1
            # if the right pointer is less than or equal to left pointer, decrement the right
            elif height[r] <= height[l]:
                r -= 1
        return res