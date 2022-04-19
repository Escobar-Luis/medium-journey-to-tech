# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

from typing import List

def partition(s: str) -> List[List[str]]:
    # initalize ans
    ans = []
    # n is length of string
    n = len(s)
    #   function to validate if word is a palindrome
    def is_palindrome(word):
        return word == word[::-1]
    
    # recurse going to take starting index and a current path
    # Index state will track what letter of the string we are on
    # path will track what words we are using to construct palindrome
    def dfs(start, cur_path):
        # if my starting index has reached the end of the string
        if start == n:
            # Then we have found a palindrom and we append a copy of our current path to our ans
            ans.append(cur_path[:])
            return
        # loop through string using start +1 to handle 0 index of string and length +1 as end to do the same
        for i in range(start + 1, n + 1):
            # every prefix will be the start variable until the current index
            prefix = s[start: i]
            # insert the prefix to our palindrome validator
            if is_palindrome(prefix):
                # If true then recursively call dfs function again.
                dfs(i, cur_path + [prefix])

    dfs(0, [])
    return ans