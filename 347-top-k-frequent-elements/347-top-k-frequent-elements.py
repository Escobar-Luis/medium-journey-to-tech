class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         track counts in hash, iterate through hash and get max, append it to res and delete key, and repeat until len(res) == k O(n^2)
#         track counts in hash, freq arr where the length == len(nums) and the index is frequency and the value at that index is gonna be a list,
        h = {}
        for n in nums:
            h[n] = 1 + h.get(n,0)
        freq = [[] for i in range(len(nums)+1)]
        for n,c in h.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) -1,-1,-1):
            for word in freq[i]:
                res.append(word)
                if len(res)==k:
                    return res
        