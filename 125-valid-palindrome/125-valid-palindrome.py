class Solution:
    def isPalindrome(self, s: str) -> bool:
        con=''
        for c in s:
            if c.isalnum():
                con +=c.lower()
        l,r = 0, len(con)-1
        while l<r:
            if con[l] != con[r]:
                return False
            l+=1
            r-=1
        return True