# Idea: divide and conquer: divide the array equally, sort each using another merge sort, and merge the two arrays back into one by having two pointers point towards the bottom of the two liss, and each step, add the smaller element from those two into the list and move the pointer of that item by one until elements from both lists are fully added
# Time Complexity: O(nlog(n)) because for each item in list, it is merged a number of times equal to the number of divisions to make to divide the list to a size of one
# Stable: because no element of the same value appears before another element with the same value in the two situations where they are either in the same or different lists
# Not In-Place: uses additional arrays to hold data

from typing import List

from numpy import sort

def sort_list(unsorted_list: List[int])-> List[int]:
    # length of given list
    n = len(unsorted_list)
    # if array contains one or two elements, we return list
    if n<=1:
        return unsorted_list
    # divide list almost evenly by using // which always returns a whole integer
    midpoint = n //2
    # recursively call sort_list on the left and right splits from the original unsorted list, 
    left_list, right_list = sort_list(unsorted_list[:midpoint]), sort_list(unsorted_list[midpoint:])
    # using an array to store data
    result_list= []
    # intializing both pointers to 0
    left_pointer, right_pointer = 0,0
    # while the left_pointer is in bounds or right pointer is in bounds
    while left_pointer < midpoint or right_pointer < n - midpoint:
        # if left pointer is at midpoint
        if left_pointer == midpoint:
            # append right_list value to res list and iterate right pointer by one
            result_list.append(right_list[right_pointer])
            right_pointer += 1
        # if right pointer is at its midpoint
        elif right_pointer == n - midpoint:
            # append left_list value to res list and iterate left pointer by one
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        # if left_list value is less than or equal to right list value
        elif left_list[left_pointer] <= right_list[right_pointer]:
            # append left list value to result array and increase left pointer by one
            result_list.append(left_list[left_pointer])
            left_pointer+= 1
        else:
            # append right list value and increase right pointer by one
            result_list.append(right_list[right_pointer])
            right_pointer += 1
        # return result list
    return result_list

if __name__ == '__main__':
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))
