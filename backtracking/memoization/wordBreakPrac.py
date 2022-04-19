from typing import List

def word_break(s: str, words: List[str]) -> bool:
    l=len(s)
    memo = {}
    def dfs(i):
        if i == len(s):
            return True

        if i in memo:
            return memo[i]

        ok = False
        for word in words:
            x=s[i:]
            if x.startswith(word):
                if dfs(i + len(word)):
                    ok = True
                    break

        memo[i] = ok
        return ok
    c=dfs(0)
    return c

word_break("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",["a", "aa", "aaa", "aaaa" ,"aaaaa", "aaaaaa", "aaaaaaa" ,"aaaaaaaa" ,"aaaaaaaaa", "aaaaaaaaaa"])