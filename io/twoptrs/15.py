from typing import List

def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            # if this isn't first value in input arr and the current value is equal to the previous value then continue because we don't want duplicates
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                # If sum is greater than 0
                if threeSum > 0:
                    r -= 1
                # If sum is less than 0
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # Because of the 2 conditions ontop updating our right pointer, we only have to update our left pointer by one if the number is a duplicate
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res