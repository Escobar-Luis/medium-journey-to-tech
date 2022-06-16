class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # h= {}
        # for s in strs:
        #     so = ''.join(sorted(s))
        #     if so in h:
        #         h[so].append(s)
        #     else:
        #         h[so] = [s]
        # return h.values()
        h = collections.defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                ind = ord('a')- ord(c)
                key[ind] +=1
            h[tuple(key)].append(s)
        return h.values()