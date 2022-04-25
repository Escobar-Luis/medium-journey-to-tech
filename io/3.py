class Solution:
# sliding window technique
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize set to keep track of duplicate characters
        # if a character is in it, then remove it and move left pointer by 1
        charSet = set()
        l = 0
        res=0
        # by just doing range, our r pointer will always be 1 after l pointer.
        for r in range(len(s)):
            # while the right is duplicate
            while s[r] in charSet:
                # remove the left character and move left by one
                charSet.remove(s[l])
                l+=1
            # if its a new character, add it to setlist
            charSet.add(s[r])
            # calculate the distance by the max between what we currently have and the difference plus 1
            res=max(res, r-l+1)
        return res