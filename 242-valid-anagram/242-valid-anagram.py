class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        o = ''.join(sorted(s))
        d = ''.join(sorted(t))
        return o == d
        