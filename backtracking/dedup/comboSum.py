# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    # our recurive func is taking a nums array, a starting index, a remaining number, and a path (combo of numbers so far)
    def dfs(nums, start_index, remaining, path):
        # If our remaining is equal to 0
        if remaining == 0:
            # we found a combo to add up to sum and we append a copy of that path to our results
            res.append(path[:])
            return
        # otherwise, we loop thorugh our start_index and the length of nums
        for i in range(start_index, len(nums)):
            # the current number during every iteration is nums[i]
            num = nums[i]
            # we then check if that number subtracted from our remaing overshoots our target by equating to negative number
            if remaining - num < 0:
                # if so, then continue
                continue
            # otherwise recall dfs but this time we update our remaining state to remaining -num and our path to path +num wrapped in list
            dfs(nums, i, remaining - num, path + [num])
    res = []
    dfs(candidates, 0, target, [])
    return res