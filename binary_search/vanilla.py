from typing import List
# Binary Search: Cut down searchable list in half durring each iteration
# Idea: The search range is represented by the left and right indices (pointers) that start from both ends of the array and move towards each other as we search. When we move the index, we discard elements and shrink the search range.
# Time Complexity: O(log(n))

# 3 key things in writing binary search:
# 1) To avoid skipping loop in scenario where array has only 1 element, use an equality comparison with while loop
# 2) Whether/how to update left and right boundary in the if conditions
# 3) Should I discard the current element?

def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:  # <= because left and right could point to the same element, just < would miss it
        # at start of every iteration, re-compute the mid to update the value to compare to target
        mid = (left + right) // 2 # double slash for integer division in python 3, we don't have to worry about integer `left + right` overflow since python integers can be arbitrarily large
        # found target, return its index
        if arr[mid] == target:
            return mid
        # middle less than target, discard left half by making left search boundary `mid + 1`
        if arr[mid] < target:
            left = mid + 1
        # middle greater than target, discard right half by making right search boundary `mid - 1`
        else:
            right = mid - 1
    return -1 # if we get here we didn't hit above return so we didn't find target