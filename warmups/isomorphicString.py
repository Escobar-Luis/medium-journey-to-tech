# Isomorphic: if each unique character from the FIRST string can be replaced to match the second string, without changing the ordering of the characters.
# Idea: When the first string is isomorphic, the lengths are the same & each unique character can only map out to either itself or another character (lets say we have to ll then l can be itself or another characteer but then that mapping stays consistent throughout the string)
# Time Complexity: O(n), where n is the size of the strings.
# Space Complexity:
# Stability:
def is_isomorphic(str_1: str, str_2: str) -> bool:
    # map to store mappings
    mapping = {}
    # set to record existence of already seen characters
    used = set() # character in str_2 already used as value in mapping
    # are the lengths of both strings not equal to each other
    if len(str_1) != len(str_2):
        # then not isomorphic
        return False
    # loop through indexes by using the length of string
    for i in range(len(str_1)):
        # intialize character from string 1
        a_char = str_1[i]
        # intialize character from string 2
        b_char = str_2[i]
        # if the current character from string 1 has already been used
        if a_char in mapping:
            # check if the value of that key which, is the character from string 1, is not equal to current character from string 2
            if mapping[a_char] != b_char:
                # if they are not, that means we would have to assign the already seen character another value which is inconsistent with an isomorphic strings
                return False
        # if this is the first time seeing this character
        else:
            # is the current character from string 2 already used
            if b_char in used:
                # if so, then we return false
                return False
            # if the string 2 character has not been used, then we add the string 1 character as our key and the string 2 character as its value pair to our hash
            mapping[a_char] = b_char
            # add the string 2 character to our set to know this character already has a mapping from string 1
            used.add(b_char)
    return True

str_1 = "Mysdd"
str_2 = "sdfll"
is_isomorphic(str_1, str_2)