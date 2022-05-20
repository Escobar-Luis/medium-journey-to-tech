from typing import List
# Bucket Sort
def topKFrequent( nums: List[int], k: int) -> List[int]:
        # hash to count ocurrences of each value
        count = {}
        # special array set to same size as input array where the index is going to be the frequency of an element, and the value is going to be the list of values that occur that particular many number of times
        freq = [[] for i in range(len(nums) + 1)]
        
        # populating hash with integer from given nums array as key and the count as value
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # index acess freq at count which is a list and append the integer to it
        # in our hash the int 1 was seen 3 times
        #in our array, we go to index 3 and append 1 there
        for n, c in count.items():
            # The value n occurs c number of times
            freq[c].append(n)
        
        res = []
        # for i in range that starts at end of our frequency array, stops at the start ( index 0), and steps backwards 1 step at a time as indicated by -1
        # we iterate through freq in reverse order so we start at the higher indexes which contain the numbers with the highest counts
        for i in range(len(freq) - 1, 0, -1):
            # for the integers at freq[i]
            for n in freq[i]:
                # we append the number to our results array
                res.append(n)
                # once we have the desired occurences, we return the array
                if len(res) == k:
                    return res
        
        # O(n)
x=[1,1,1,2,2,3]
topKFrequent(x,2)