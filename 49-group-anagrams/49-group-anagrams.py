class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # h=collections.defaultdict(list)
        # for s in strs:
        #     freq = [0] * 26
        #     for c in s:
        #         ind = ord(c)-ord('a')
        #         freq[ind] +=1
        #     h[tuple(freq)].append(s)
        # return list(h.values())
        h=collections.defaultdict(list)
        for s in strs:
            so = ''.join(sorted(s))
            h[so].append(s)
        return list(h.values())
            
                