link_to_problem = 'https://leetcode.com/problems/find-smallest-letter-greater-than-target/'

# The problem is the same as finding the boundary of elements that are less than 3 and those that are greater or equal to 3
# That in itself will be the boolean statement we use as an if statement (a.k.a filter) during our binary serach
# If the current index value is larger than 3 than we save that index in our boundary, and disregard it and everything to its right.

from typing import List

def first_not_smaller(arr: List[int], target: int) -> int:
    # Initiate left and right pointers, where right pointer is set to the length of the given array - 1 because python reads list starting at 0 not 1 so we subtract 1 from our right pointer to make sure that it is in bounds.
    left, right = 0, len(arr) - 1
    # Track of the leftmost index of the element that is larger than or equal to target (a.k.a makes this statement true). Also, since we are guaranteed to find a satisfying number per question constraints, the intitating number can be anything since it will be updated in the future.
    boundary_index = -1
    # Note the equality to make sure either pointer never cross to each others respective domains
    while left <= right:
        # recalculate mid in every iteration by using the new values of left and right pointers
        mid = (left + right) // 2
        # if mid of our array's value is greater than or equal to the given target
        if arr[mid] >= target:
            # we set the boundary index to our mid since we have to return the index of the element that satisfies condition
            boundary_index = mid
            # move right pointer to mid and subtract one from it to disregard the mid element as well
            right = mid - 1
        # the mid value is less than or equal to the given target
        else:
            # move left pointer to mid and ADD one to it to disregard the mid element as well
            left = mid + 1
    # return boundary index after sorting whole array
    return boundary_index