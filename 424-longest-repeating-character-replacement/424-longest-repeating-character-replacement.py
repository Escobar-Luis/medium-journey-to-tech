class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        res = 0
        maxf = 0
        l = 0
        for r in range(len(s)):
            h[s[r]] = 1+ h.get(s[r],0)
            maxf = max(maxf, h[s[r]])
            
            while r-l+1 - maxf >k:
                h[s[l]] -=1
                l+=1
            res = max(res, r-l+1)
        return res