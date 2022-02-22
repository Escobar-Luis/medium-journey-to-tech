# Idea: for each iteration, we use a pointer to point at the first element fo the list, For each cycle, we compare it to the mex element in the list aand swap themif the current item is greater, them mocethe pointer by one until it reaches the end of the list and, then move the pointer by one until it reaches the end of the list and we know the list is sorted if during a pass no swapping occurs
# Time Complexity: O(n^2) because we are using two loops
# Stable because a swap cannot cause an element of same value to move past another
# In_place because no addtional data structure is used

from typing import List

def sort_list(unsorted_list: List[int])-> List[int]:
    # n is the length of the number array
    n=len(unsorted_list)
    # looping through entire array in reverse order
    for i in reversed(range(n)):
        # keeping track if we swap during current iteration and using i as our pointer
        swapped = False
        # nested loop through entire array
        for j in range(i):
            # if our current value is greater than the next value
            if unsorted_list[j] > unsorted_list[j+1]:
                # we swap them
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
                # set swap to True and our reversed range moves our pointer by one
                swapped = True
        # if no swap occured during the loop, then our array is sorted and we return that array
        if not swapped:
            return unsorted_list
    return unsorted_list

if __name__ == '__main__':
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))