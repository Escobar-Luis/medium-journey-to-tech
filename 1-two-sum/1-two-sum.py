class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i,n in enumerate(nums):
            need = target - n
            if need in h:
                return [h[need], i]
            h[n] = i