class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         1: Hash, pass through arr, sort every word, save the sorted word as key in hash and append original, return values
        # h = {}
        # for s in strs:
        #     sort = ''.join(sorted(s))
        #     if sort in h:
        #         h[sort].append(s)
        #     else:
        #         h[sort] = [s]
        # return h.values()
        
        # 2: hash, pass through arr, create arr containing 26 0s, for every letter in word subtract ordinal(a) from it and use it to iterate index count, then save count to hash and append word to it
        h = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                pos = ord('a') - ord(c)
                count[pos] +=1
            x=tuple(count)
            if x in h:
                h[x].append(s)
            else:
                h[x] = [s]
        return h.values()