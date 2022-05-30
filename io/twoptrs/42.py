from typing import List

def trap(height: List[int]) -> int: 
    if not height: return 0
    
    l, r = 0, len(height) - 1
    # the maxes are going to be our bottleneck on each side
    leftMax, rightMax = height[l], height[r]
    res = 0
    # every iteration we check which bottleneck is smaller so we shift that sides pointer and recalulate that sides max seen so fat
    while l < r:
        # shift the smaller max because that is the bottleneck
        if leftMax < rightMax:
            # move left if our leftMax is smaller than rightMax
            l += 1
            # We update leftMax to either the Max seen to our new height value at the newly shifted l pointer
            leftMax = max(leftMax, height[l])
            # we add the difference between leftMax and current height to our result
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res