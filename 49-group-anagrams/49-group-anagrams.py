class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O (m*n)
        h = collections.defaultdict(list)
        for word in strs:
            key = [0]*26
            for c in word:
                ind = ord('a')-ord(c)
                key[ind] +=1
            h[tuple(key)].append(word)
        return h.values()