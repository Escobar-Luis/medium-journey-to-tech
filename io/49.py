#Group Anagrams
from tokenize import group
from typing import List
import collections
# Time Complexity is O(m * n) where m is length of list of strings strs and n is the maximum length of a string in strs.
def groupAnagrams(strs: List[str]) -> List[List[str]]:
        # ans is our hash which takes the count as a key and the anagrams grouped together in a list as a value
        # by using a default dict we can handle edge case where the hash does not exist
        ans = collections.defaultdict(list)
        # For every word in the list
        for s in strs:
            # every pass for each word, we set count to a list of 26 0's
            count = [0] * 26
            # every pass for each character in a word, we figure out each character unicode value and iterate its count by one then we access or create key in hash using tuple count and append the current interations word in it. 
            for c in s:
                # ord method converts a character to its unicode value so we can track which character is alphanumerical or a special character
                first = ord(c)
                sec=ord('a')
                # the index can be given by subtracting the unicode values
                diff=ord(c) - ord('a')
                # acess the index of the specific character
                h=count[diff]
                count[diff] += 1
            # we change count list to a tuple because they are immutable yet list are which is a no no for python dicts
            ans[tuple(count)].append(s)
        return ans.values()

x=["eat","tea","tan","ate","nat","bat"]
groupAnagrams(x)