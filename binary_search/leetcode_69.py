link_to_problem = 'https://leetcode.com/problems/sqrtx/'
# Given an integer we have to find its square root without using a built-in square root function and disregard the decimal places, only return whole integer
# Meaning find y < Square root of given n, which can be re-written as y^2 < given n
# Since we are given n, we just have to find the m
# The problem is equivalent to finding the boundary of elements < n and elements >= n.
# If we apply a filter of the value * value = n (A.K.A return boolean where value squared = n) then the problem is reduced to finding the last true element in a boolean array.


def square_root(n: int) -> int:
    # We handle edge case of the integer being equal to 0
    if n == 0:
        return 0
    # construct left and right pointers where the right pointer is equal to the given number
    left, right = 1, n
    # construct of boundary index
    res = -1
    # Make sure the pointers never cross each other by using a equality operator
    while left <= right:
        # At start of every iteration, re-construct midpoint
        mid = (left + right) // 2
        # If midpoint squared id less than or equal to our given number
        if mid * mid <= n:
            # update boundary index to mid and move right pointer
            res = mid
            left = mid + 1
        # else if mid is larger than midpoint
        else:
            # Move the right pointer
            right = mid - 1
    return res