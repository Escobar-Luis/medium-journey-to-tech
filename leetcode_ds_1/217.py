class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # intialize hashmap to keep track of numbers we have seen
        # Takes O(1) - constant time
        h={}
        # Independent pass to iterate through n elements in array which is O(n)- linear time
        for i,v in enumerate(nums):
            # boolean comparison - constant time O(1)
            if v in h:
                return True
            # variable assignment - constant time O(1)
            h[v] = i
        return False
    
    # Time complexity is O(n) Linear time