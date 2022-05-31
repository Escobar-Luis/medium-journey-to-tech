class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#         At every position I want to calculate my prefix and postfix and multiply those together
#         res = [1] for i in range(len(nums))
#         prefix =1
#         first pass, we update our res[i] to prefix, and then update prefix to product of current value to nums[i]
#         postfix=1
#         second pass backwards, we update our res[i] not to postfix but the product of the indexes prefix at res[i] with the postfix, and then update postfix to product of itself with nums[i]
# return res
        res = [1] * len(nums)
        prefix =1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix =1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res