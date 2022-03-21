def anagram (l):
    hash = {}
    for string in l:
        sorted_string = ''.join(sorted(string))
        if sorted_string in hash:
            hash[sorted_string].append(string)
        else:
            hash[sorted_string] = [string]
    x =list(hash.values())
    return x

anagram(["eat" ,"tea", "tan", "ate", "nat", "bat"])