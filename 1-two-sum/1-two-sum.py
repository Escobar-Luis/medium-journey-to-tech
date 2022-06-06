class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h={}
        for i,v in enumerate(nums):
            n = target-v
            if n in h:
                return [i, h[n]]
            h[v] = i
        