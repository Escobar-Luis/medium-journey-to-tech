class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#       To ask it a question if the needed number has been seen before
        h={}
        for i in range(len(nums)):
            req= target-nums[i]
            if req in h:
                return [h[req],i]
            h[nums[i]] = i