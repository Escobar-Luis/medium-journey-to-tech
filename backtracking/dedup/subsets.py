# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    # n is the length of the nums
    n = len(nums)
    # ans
    res = []
    # takes in index and current num
    def dfs(i, cur):
        # reached end of nums list
        if i == n:
            # append current numb to result
            res.append(cur)
            return
        # call dfs on current number + current and just current number
        dfs(i + 1, cur + [nums[i]])
        dfs(i + 1, cur)
    # call dfs starting from 0 and passing empty array
    dfs(0, res)
    # return the res
    return res

def subsets_dedup(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    # one change it result is a list of list
    res = [[]]
    def dfs(i, cur):
        # if we reach end, we dont do anything but bubble up recursion
        if i == n:
            return
        # we append cur +number to result
        res.append(cur + [nums[i]])
        dfs(i + 1, cur + [nums[i]])
        dfs(i + 1, cur)
    dfs(0, [])
    return res