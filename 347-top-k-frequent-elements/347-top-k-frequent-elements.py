class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        h= {}
        for n in nums:
            h[n] = 1+ h.get(n,0)
        for n,c in h.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res