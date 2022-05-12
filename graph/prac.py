# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# I merge when the  arr[1](greatest num) >= newInterval[0](least num): lowerbound
# min(arr[0],newInterval[0]), max(arr[])
# newInterval[0] >= arr[0] 
# Input: intervals = [[1,2],[4,5],[1,7],[3,10],[12,16]], newInterval = [3,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

# [1,4] [2,3] Overlap within [min(arr[0],newInterval[0]), max(arr[1],newInterval[1])]
# [1,4] [4,5] Overlap Out
# [1,4] [1,7] Overlap in

def insertInterval(interval, newInterval):
    res=[]
    print(newInterval[0],newInterval[1])
    for arr in interval:
        
        res.append(arr)
        if newInterval[0] >= arr[0]:
            

print(
    insertInterval(
        [[1,3],[6,9]],
        [2,5]
    )
) # [[1,5],[6,9]]