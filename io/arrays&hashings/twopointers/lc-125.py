class Solution:
    def isPalindrome(self, s: str) -> bool:
#       Remove all non-alphanumeric characters
#       We are iterating through each character n and doing constant work at each iteration makeing it o(n)
        s = ''.join(char for char in s if char.isalnum())
#     reversign string takes O(n) work
        r = s[::-1]
        print(s.lower())
        print (r.lower())
        if s.lower() !=r.lower():
            return False
        return True