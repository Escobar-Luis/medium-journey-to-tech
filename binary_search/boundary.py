from typing import List
# Binary Search with boundary_index : Boundary_index is updated if similar element found to but not sure if it is the first appearnace
# Idea: Two things to decide while searching, if the element is not it, then disregard that element and everything to its side (in this case left). Other thing is if the element is it, how do we know if it is the first apperance? Well, we save its index in a variable and disregard that element and everything to its side (in this case right) until we exit our for loop when pointers go out of bounds.
# Time Complexity: O(log(n))
def find_boundary(arr: List[bool]) -> int:
    # Create left and right pointers
    left, right = 0, len(arr) - 1
    # if desired element is not in given array, then we're instructed to return -1. Since the boundary_index is going to be our return value than we create it with an intial value of -1 and update it in the while loop if needed
    boundary_index = -1
# Stop loop when left and right pointers are on same index
    while left <= right:
        # construct midpoint
        mid = (left + right) // 2
        # if the value is true
        if arr[mid]:
            # update boundary index to current mid
            boundary_index = mid
            # disregard current mid & everything to its right
            right = mid - 1
        # Only other scenario can be if the mid is false
        else:
            # if true, then disregard current mid and everything to its right 
            left = mid + 1
    # at end of loop, return boundary index variable.
    return boundary_index