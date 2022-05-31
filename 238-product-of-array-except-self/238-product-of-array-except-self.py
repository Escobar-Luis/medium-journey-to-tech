class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#   result array with 1s up to length of nums array, I first calculate the prefixes at every position and multiply to my results arr, then calculate the postfixes and multiply them to my results array and then return result
        res = [1] * len(nums)
        prefix=1
#         set res[i] to prefix and update it to the new value
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res