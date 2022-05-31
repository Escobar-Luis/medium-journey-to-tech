class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         1: Hash, pass through arr, sort every word, save the sorted word as key in hash and append original, return values
        h = {}
        for s in strs:
            sort = ''.join(sorted(s))
            if sort in h:
                h[sort].append(s)
            else:
                h[sort] = [s]
        return h.values()