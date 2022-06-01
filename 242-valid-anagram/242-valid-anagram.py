class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h1 = {}
        h2 = {}
        for i in range(len(s)):
            h1[s[i]] = 1 + h1.get(s[i],0)
            h2[t[i]] = 1 + h2.get(t[i],0)
        for c in s:
            if c not in h2 or h1[c] != h2[c]:
                return False
        return True