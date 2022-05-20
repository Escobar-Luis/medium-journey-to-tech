"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
# """
# Add the length of string, A symbol, and the string to know how many characters after pound is the length of string
def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

"""
@param: str: A string
@return: dcodes a single string to a list of strings
"""
def decode(str):
    res, i = [], 0

    while i < len(str):
        # Find the delimiter (the end of the integer)
        j = i
        # while we still are at an integer character, we keep incrementing until we get to pound character
        while str[j] != "#":
            j += 1
        # the length of string will be the number that comes before the pound sign
        length = int(str[i:j])
        # j+1 is the first character in string (skipping delim) to j+1+length of string we calculated
        res.append(str[j + 1 : j + 1 + length])
        # we update i to the beginning of the next string
        i = j + 1 + length
    return res

decode(encode(["lint","code","love","you"]))