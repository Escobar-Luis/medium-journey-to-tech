class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in nums:
            if n-1 not in s:
                l = 1
                while n+l in s:
                    l+=1
                res = max(res,l)
        return res
                