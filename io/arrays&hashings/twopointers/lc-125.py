class Solution:
    def isPalindrome(self, s: str) -> bool:
#       Remove all non-alphanumeric characters
#       We are iterating through each character n and doing constant work at each iteration makeing it o(n)
        # I am increasing space complexity by creating a new version oof the string
        s = ''.join(char for char in s if char.isalnum())
#     reversign string takes O(n) work
        r = s[::-1]
        print(s.lower())
        print (r.lower())
        if s.lower() !=r.lower():
            return False
        return True
    
class Solution2:
# Our time complexity is the same as above but our space complexity is better since we don't have to use a tmp variable
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]): 
                l += 1
            while l < r and not self.alphanum(s[r]): 
                r -= 1
            if s[l].lower() != s[r].lower(): 
                return False
            l += 1
            r -= 1
        return True
    
    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))