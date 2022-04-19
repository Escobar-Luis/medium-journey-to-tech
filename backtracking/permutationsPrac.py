from typing import List

def permutations(letters: str) -> List[str]:
    def dfs(path,used,res):
       #We know we found a solution if the length of path is equal to the length of our letters
        if len(path)==len(letters):
            res.append(''.join(path))
            return
        #Loop though letters
        for i,letter in enumerate(letters):
            #We check if the letter has been used in path
            if used[i]:
                continue
            #add it to path, set used to True, and recurse onto next letter
            path.append(letter)
            used[i]=True
            dfs(path,used,res)
            #clean path, set used to False
            path.pop()
            used[i]=False
        return res
    return dfs([],[False]*len(letters),[])