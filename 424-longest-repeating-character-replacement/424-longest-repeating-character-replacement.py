class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        long=0
        maxf=0
        l=0
        for r in range(len(s)):
            h[s[r]] = 1+ h.get(s[r],0)
            maxf = max(h[s[r]], maxf)
        
            while r-l+1 - maxf >k:
                h[s[l]] -=1
                l+=1
            long = max(long, r-l+1)
        return long
