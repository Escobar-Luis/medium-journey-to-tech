class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        # o = ''.join(sorted(s))
        # d = ''.join(sorted(t))
        # return o == d
        ho={}
        hd={}
        for i in range(len(s)):
            ho[s[i]]= 1 + ho.get(s[i],0)
            hd[t[i]]= 1 + hd.get(t[i],0)
        
        for n in s:
            if n not in hd or ho[n] != hd[n]:
                return False
        return True
        