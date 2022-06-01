class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort
        h = {}
        freq= [[] for i in range(len(nums)+1)]
        for n in nums:
            h[n] = 1+ h.get(n,0)
        res = []
        for n,c in h.items():
            freq[c].append(n)
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            