class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        # First pass o(n)
        for i,v in enumerate(nums):
            # make sure not first iteration and that previous character is not duplicate
            if i>0 and v == nums[i-1]:
                continue
            l,r= i +1, len(nums)-1
            # second pass increasing time complexity to o(n^2)
            while l<r:
                s = v + nums[l] + nums[r]
                if s > 0:
                    r -=1
                elif s<0:
                    l+=1
                else:
                    res.append([v,nums[l],nums[r]])
                    l+=1
                    # make sure that the left pointer does not go out of bounds with l<r
                    while nums[l] ==nums[l-1] and l<r:
                        l+=1
        return res