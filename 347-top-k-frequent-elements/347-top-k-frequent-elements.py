class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         hash, pass through nums, add count to hash, while res length <k, insert max value key to result and delete from hash, return res
        h = {}
        res = []
        for n in nums:
            h[n] = 1 + h.get(n,0)
        while len(res) <k:
            maxKey = max(h, key=lambda k: h[k])
            res.append(maxKey)
            del h[maxKey]
        return res