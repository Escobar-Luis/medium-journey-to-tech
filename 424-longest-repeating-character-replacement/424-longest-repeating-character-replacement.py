class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        h= {}
        maxF = 0
        l = 0
        for r in range(len(s)):
            h[s[r]] = 1 + h.get(s[r],0)
            maxF = max(h[s[r]], maxF)
            
            while r-l+1 - maxF > k:
                h[s[l]] -=1
                l+=1
            res = max(res, r-l+1)
        return res