# Idea: During each iteration, find smallest item from unsorted_pile and we add it to our tmp sorted pile
# In-Place because a tmp variable is only used to hold data
# Algo is not stable because an earlier element can jump after an element of same value during the swap
# Time Complexity is O(n^2)

from typing import List

def sort_list (unsorted_list: List[int]) -> List[int]:
    # n is the length of the unsorted list
    n= len(unsorted_list)
    # Looping thorugh all array elements in number array
    for i in range(n):
        # tmp variable keeping track of the the index of the smallest element (position)
        min_index = i 
        # Finding the minimum element in the remaining unsorted_array
        for j in range(i,n):
            # if current value during iteration is less than the min_index, 
            if unsorted_list[j] < unsorted_list[min_index]:
                # than we set the min_index to j to know where the elements position is
                min_index = j
        # During each iteration, we swap out the found minimum element with the first element
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]
    print(unsorted_list)

# Boiler plate code that protexts users from accidently invoking the script
# if __name__=='__main__':
#     unsorted_list = [int(x) for x in input().split()]
#     res= sort_list(unsorted_list)
#     print(" ".join(map(str, res)))
    
sort_list([2,3,5,6,4,6,4,5,6])