# Given a string of unique letters, find all of its distinct permutations.

from typing import List
# What state do we need to know whether we have reached a solution (and using it to construct a solution if the problem asks for it).
# We need a state to keep track of the list of letters we have chosen for the current permutation (path variable)

# What state do we need to decide which child nodes should be visited next and which ones should be pruned.
# We have to know what are the letters left that we can still use (since each letter can only be used once). (used variable)
def permutations(letters):
    # We are using path to keep track of nodes we visited so we can use them to construct a combo when we reach leaf nodes
    # We are using a used variable to know what letters we can use
    def dfs(path, used, res):
        if len(path) == len(letters):
            res.append(''.join(path))
            return

        for i, letter in enumerate(letters):
            # skip used letters
            if used[i]:
                continue
            # add letter to permutation, mark letter as used
            path.append(letter)
            used[i] = True
            dfs(path, used, res)
            # remove letter from permutation, mark letter as unused
            path.pop()
            used[i] = False

    res = []
    dfs([], [False] * len(letters), res)
    return res