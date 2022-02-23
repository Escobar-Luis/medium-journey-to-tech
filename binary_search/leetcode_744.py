link_to_problem = 'https://leetcode.com/problems/find-smallest-letter-greater-than-target/'

# The problem is the same as finding the boundary of elements that are less than 3 and those that are greater or equal to 3
# That in itself will be the boolean statement we use as an if statement (a.k.a filter) during our binary serach
# If the current index value is larger than 3 than we save that index in our boundary, and disregard it and everything to its right.

from typing import List

def first_not_smaller(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index