class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#         We know a value is a start of a sequence if its previous value need is not in set
        s = set(nums)
        res = 0
        for n in nums:
            if (n-1) not in s:
                tmp =1
                while (n+tmp) in s:
                    tmp+=1
                res = max(res,tmp)
        return res
            