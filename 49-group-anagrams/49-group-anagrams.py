class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h= {}
        for s in strs:
            so = ''.join(sorted(s))
            if so in h:
                h[so].append(s)
            else:
                h[so] = [s]
        return h.values()