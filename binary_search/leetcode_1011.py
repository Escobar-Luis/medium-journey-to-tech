link_to_problem = 'https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/'

# At minimum, if our truck capacity is only 1 package, we need the max(weights) days to ship all packages.

# At maximum, if our truck capacity is sum(weights), then it'd take only 1 day to ship.

# Since we want to ship within d days, the optimal truck capacity somewhere in between.

# We know how to find if a truck capacity is feasible or not - we simply loop through the weights and see if we can ship it within d days. Now this has yet again turned into the classic Finding the Boundary problem.

# Note that there is a simplification above. The minimum is actually max(weights) since our truck has to be able to at least fit the item of largest weight.

class Solution(object):
    def shipWithinDays(self, weights, d):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def feasible(weights, max_weight, d) :
            req_days = 1
            capacity = max_weight
            i = 0
            n = len(weights)
            while i < n:
                if weights[i] <= capacity:
                    capacity -= weights[i]
                    i += 1
                else:
                    req_days += 1
                    capacity = max_weight
            return req_days <= d
        
        min_ptr = max(weights)
        max_ptr = sum(weights)
        boundary_index = max_ptr
        while min_ptr <= max_ptr:
            midpoint = (min_ptr + max_ptr) // 2
            if feasible(weights, midpoint, d):
                boundary_index = midpoint
                max_ptr = midpoint - 1
            else:
                min_ptr = midpoint + 1
        return boundary_index