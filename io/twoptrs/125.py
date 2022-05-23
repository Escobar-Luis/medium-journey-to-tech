# Problem with basic solution:
# 1) Using extra memory by creating newStr variable
# 2) Using a built in funciton to tell if character is alphanumercial
def isPalindrome_Basic(self, s: str) -> bool:
    # Create New String variable
    newStr=''
#    pass through every character in original string
    for c in s:
    # if the character is alpha numeric
       if c.isalnum():
        #    Then add the lowercase version of that string to our NewStr variable
           newStr += c.lower()
    # Check if newStr is equal to reversed newStr
    return newStr == newStr[::-1]


# Optimal 2 pointer solution
# Theory: a palindrome reads the same backwards, so a left pointer starting at the front and a right pointer starting from end should equal each other
# To bypass nonalphanumerical characters, during while loop we check if the character from either l or r pointer doesn't matter, we just move that pointer
def isPalindrome(self, s: str) -> bool:
    
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not alphanum(s[l]): 
            l += 1
        while l < r and not alphanum(s[r]): 
            r -= 1
        if s[l].lower() != s[r].lower(): 
            return False
        l += 1
        r -= 1
    return True

# Could write own alpha-numeric function
def alphanum(self, c):
    return (
            # If Ascii value of character is uppercase (if char is uppercase?)
            ord('A') <= ord(c) <= ord('Z') or
            # # If Ascii value of character is lowercase (if char is lowercase?)
            ord('a') <= ord(c) <= ord('z') or
            # If Ascii value of character is numerical (if char is a number?)
            ord('0') <= ord(c) <= ord('9'))