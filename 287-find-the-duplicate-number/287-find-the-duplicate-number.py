class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h = {}
        
        for n in nums:
            if n in h:
                return n
            else:
                h[n] = n
        