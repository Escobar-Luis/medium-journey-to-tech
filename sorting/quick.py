# Idea: select pivot (arbitrary element), and swap elements in the list into two sides, one side where all elements are larger than pivot and one side where all elements are smaller than pivot. After we swap the pivot with the first element of the side that is larger or equal to the pivot. Then just sort the left interval and the right interval using the same method, then the list would be sorted
# Time Complexity: O(nlog(n)) if listed divided near the center. If the pivot point chosed is at end of list and the list is already sorted than, worst case is O(n^2)
# Not Stable: Each swap skips alot of values
# In-Place: No additional data structures needed.
# Not constant space as it uses recursion as its core logic and min recurive layers are equal to log(n).

from typing import List

def sort_list_interval(unsorted_list: List[int], start: int, end: int) -> None:
    # if the list is empty than return nothing
    if end - start <= 1:
        return
    # choosing pivot as element right before the end
    pivot = unsorted_list[end - 1]
    # starting pointer is the given start
    start_ptr = start
    # end pointer is one less than given end
    end_ptr = end - 1
    # while starting pointer has not intersected end pointer
    while start_ptr < end_ptr:
        while unsorted_list[start_ptr] < pivot and start_ptr < end_ptr:
            start_ptr += 1
        while unsorted_list[end_ptr] >= pivot and start_ptr < end_ptr:
            end_ptr -= 1
        if start_ptr == end_ptr:
            break
        # swap start ptr value with end and end pointer value with start
        unsorted_list[start_ptr], unsorted_list[end_ptr] = unsorted_list[end_ptr], unsorted_list[start_ptr]
    # swap start ptr value with element before end of list and that same value with the start_ptr value
    unsorted_list[start_ptr], unsorted_list[end - 1] = unsorted_list[end - 1], unsorted_list[start_ptr]
    # recursive call giving the list and start and end points
    sort_list_interval(unsorted_list, start, start_ptr)
    sort_list_interval(unsorted_list, start_ptr + 1, end)

def sort_list(unsorted_list: List[int]) -> List[int]:
    sort_list_interval(unsorted_list, 0, len(unsorted_list))
    return unsorted_list

if __name__ == '__main__':
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))