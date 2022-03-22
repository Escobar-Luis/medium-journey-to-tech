link_to_problem = 'https://leetcode.com/problems/peak-index-in-a-mountain-array/'

# A mountain array is defined as an array that

# has at least 3 elements
# let's call the element with the largest value the "peak", with index k. The array elements monotonically increase from the first element to A[k], and then monotonically decreases from A[k + 1] to the last element of the array. Thus creating a "mountain" of numbers.
# That is, given A[0]<...<A[k-1]<A[k]>A[k+1]>...>A[n-1], we need to find the index k.

# Find the index of the peak element. Assume there is only one peak element.

# The peak element is always larger than the next element. Applying the filter of arr[i] > arr[i + 1] we get a boolean array. A minor edge case is for the last element as it has no next element. In that case, we assume its next element is negative infinity.

# Now the problem is reduced to finding the first true element in a boolean array. And we already know how to do this from Find Boundary module.
from typing import List

def peak_of_mountain_array(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        # Peak element always has to be larger than the next element since we assume there is only 1 peak
        if arr[mid] > arr[mid + 1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index