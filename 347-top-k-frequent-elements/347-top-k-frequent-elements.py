class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         Bucket Sort: hash for count, freq arr === size of nums where ind is freq and value is a list of nums appearing that many times, loop backwards through freq arr and for every number at that freq, we append it to our results while len(res)==k
        h = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            h[n] = 1 + h.get(n,0)
        for n,c in h.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res