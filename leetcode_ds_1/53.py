def maxSubArray(array):
	maxSum = min(array) #Initializing maxSum to min array value
	n = len(array)
	for i in range(n):
            first = array[i]
            for j in range(i, n): 
                second=array[j]
                sum = 0
                for k in range(i, j + 1):
                        third=array[k]
                        sum = sum + array[k]	# Finding the sum of the subarray from ith to jth element
                        maxSum = max(maxSum, sum) 	# If current sub array sum is greater than maxSum, updating maxSum	
            return maxSum

maxSubArray([-2,1,-3,5,20])