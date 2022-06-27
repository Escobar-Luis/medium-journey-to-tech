class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hs = {}
        ht = {}
        for i in range(len(s)):
            hs[s[i]] = 1+ hs.get(s[i],0)
            ht[t[i]] = 1+ ht.get(t[i],0)
        for c in hs:
            if hs[c] != ht.get(c,0):
                return False
        return True