from typing import List
def productExceptSelf(nums: List[int]) -> List[int]:
    # res is a list containing 1 at every index with a length equal to the amount of given numbers
        res = [1] * (len(nums))
        
        prefix = 1
        # iterating through nums normal
        for i in range(len(nums)):
            # We set res[i] to prefix
            res[i] = prefix
            # update prefix with nums[i]
            prefix *= nums[i]
        postfix = 1
        # iterating through nums manga style
        for i in range(len(nums) - 1, -1, -1):
            # we set res[i] to the product of our postfix and original pre-fix stored their during our first pass
            res[i] *= postfix
            # update postfix with nums[i]
            postfix *= nums[i]
        return res
productExceptSelf([1,2,3,4])