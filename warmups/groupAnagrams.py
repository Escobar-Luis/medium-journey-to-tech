from typing import List
# Anagram: when an elements has same characters and can be in different order
# Idea: When two strings are anagrams; if we sort both strings by character, then the new sorted string will result in the same value. If the strings are not anagrams, the sorted string will result in a different value
# Time Complexity: O(n*mlog(m)), n is the number of strings and m is the max size of each string
# Space Complexity:
# Stability:
def group_anagrams(strs: List[str]) -> List[List[str]]:
    # Has map stores key as 'anagram ID' (sorted value of string) & its value being a list of strings with the same sorted string value.
    anagram_map = {}
    # iterating through every string in the array
    for entry in strs:
        # we use built in sorted function on each string in list which takes an iterable (our string) and breaks it apart into a subarray of letters in sorted order
        # to combine the sorted letters into a word again, we join it with no seperator ('')
        anagram_id = "".join(sorted(entry))
        # if the sorted entry is in our hashmap
        if anagram_id in anagram_map:
            # we add the original entry as a value to our sorted entry key
            anagram_map[anagram_id].append(entry)
            # if anagram id is not in our hashmap
        else:
            # we set our sorted entry as our key, and the original entry as our value in array format so we can keep appending anagrams to this key
            anagram_map[anagram_id] = [entry]
        x=list(anagram_map.values())
        # we return a list of strings for each anagram_id's values
    return list(anagram_map.values())

group_anagrams(["eat" ,"tea", "tan", "ate", "nat", "bat"])