from typing import List

# Time Complexity is O(n^2) [ O(n * (n-1)/2) ] because you have to store each number in an array and multiply them after
# Stable Algo because the relative order of numbers is maintained or the original order of equal keys if maintained
# In-Place Algo because no tmp data is held

def sort_list (unsorted_list: List[int]) -> List[int]:
    # looping thourgh nums array getting every index and value of current iterataion
    for i, entry in enumerate(unsorted_list):
        # we name our index as our current value
        current = i
        # while the iteration isn't the first and the value of this iteration is less than the previous iteration
        while current > 0 and unsorted_list[current] < unsorted_list[current-1]:
            # we equate the current iteration's value to the previous iteration because it is smaller and the previous iteration to our current value because it is greater
            unsorted_list[current], unsorted_list[current-1] = unsorted_list[current-1], unsorted_list[current]
            # we then shift our current index back 1 so we can compare the switched value to the previous value before the iteration to make sure the newly switched value is still less than the prviously iterated value
            current -=1
        # the we return the sorted list
        return unsorted_list
    
if __name__=='__main__':
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(' '.join(map(str,res)))
    
