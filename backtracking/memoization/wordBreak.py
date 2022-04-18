# Given a string and a list of words, determine if the string can be constructed from concatenating words from the list of words. A word can be used multiple times.

# we are taking a string, and words to check if the words can be used to equate string
def word_break(s, words):
    # Recursive call, taking in index
    def dfs(i):
        # If index is equal to length of string, then we have constructed our string
        if i == len(s): # we have constructed the entire target s
            # We return true
            return True
        # We loop through every word in words
        for word in words:
            # We check if any letters from string contain the word on first iteration
            if s[i:].startswith(word): # is this a valid path
                # If so then we add the length of the word to i since access to array is 0 indexed and we want to skip the word we just found
                if dfs(i + len(word)):
                    # If we reach our base case where i is equal to length of string, then we return true
                      return True # any path leads to true is fine
        # if nothing above is true, then we return false
        return False

    return dfs(0)

def word_break_memo(s, words):
    # We intialize memo outside recursive function
    memo = {}
    def dfs(i):
        # If index is equal length of string we are trying to matcb
        if i == len(s):
            # We have successfully recreated string, so we can return True
            return True
        # If index is in memo (meaning we have seen this before)
        if i in memo:
            # Then we just return ok which can be either False or True
            return memo[i]
        # we set ok to false at every new node
        ok = False
        # We iterate through every node
        for word in words:
            # if everything after what we have matched so far matches new word or old word again
            if s[i:].startswith(word):
                # we recurively call function again on the next index after filling in word
                if dfs(i + len(word)):
                    # If we return True, then we set ok to true
                    ok = True
                    break
        # We cache our result in memo[i]
        memo[i] = ok
        # we return ok boolean at end of recurive call 
        return ok
    return dfs(0)