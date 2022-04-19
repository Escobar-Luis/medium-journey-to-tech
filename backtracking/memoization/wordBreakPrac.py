def word_break(s: str, words: List[str]) -> bool:
    def dfs(path,s):
        if len(path)==len(s):
            return True
        for word in words:
            if s.startswith(word):
                path.append(word)
                dfs(path,s[len(word):len(s)])
        return False
    return dfs([],s)

word_break("algomonster",["algo", "monster"])