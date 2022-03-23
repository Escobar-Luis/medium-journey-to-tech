# A sorted array was rotated at an unknown pivot. For example, [10, 20, 30, 40, 50] becomes [30, 40, 50, 10, 20]. Find the index of the minimum element in this array. Also, return the minimum index if the minimum number is repeated.
# It may seem like we can't use binary search because the array is not sorted but we can since there is a binary decision we can use to shrink the search range!
# If we were to plot a given input onto a line graph, we would be able to notice that the numbers are divided into 2 sections:
# Numbers larger than the last element of the array and numbers smaller than it
# So we know that the minimum element is at the boundary between these two sections
# We can apply a filter of being less than the last element to get a boolean array that characterizes the two sections
# A pattern is reducing problems to a boolean array so we could just find the first true elemnt in a boolean array using a boundary index.d

from typing import List

def find_min_rotated(arr: List[int]) -> int:
    # initialize left and right pointers
    left, right = 0, len(arr) - 1
    # Init boundary index to track index
    boundary_index = -1
    #init while loop with equality to stop pointers from crossing each other 
    while left <= right:
        # re-construct mid at start of every iteration
        mid = (left + right) // 2
        # if <= last element, then belongs to lower half
        if arr[mid] <= arr[-1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index