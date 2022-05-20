from typing import List

def longestConsecutive(self, nums: List[int]) -> int:
    # set to keep track of nums seen
    numSet = set(nums)
    # longest variable
    longest = 0
    # iterate through nums
    for n in nums:
        # check if its the start of a sequence
        if (n - 1) not in numSet:
            # if not in sequence, reset the length of current sequence to 1
            length = 1
            # If n + length in numset, then increment length by one
            while (n + length) in numSet:
                length += 1
            # Longest is the max between current length and the longest seen so far
            longest = max(length, longest)
    return longest