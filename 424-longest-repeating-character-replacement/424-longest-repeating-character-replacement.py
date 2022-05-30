class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        l = 0
        res = 0
        maxF = 0
        for r in range(len(s)):
            h[s[r]] = 1 + h.get(s[r],0)
            maxF = max(maxF, h[s[r]])
            while (r-l+1) - maxF >k:
                h[s[l]] -=1
                l+=1
            res = max(res, r-l+1)
        return res