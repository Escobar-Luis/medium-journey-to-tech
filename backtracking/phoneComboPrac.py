from typing import List

cyph={
2:'ABC',
3:'DEF',
4:'GHI',
5:'JKL',
6:'MNO',
7:'PQRS',
8:'TUV',
9:'WXYZ'
}
def letter_combinations_of_phone_number(digits: str) -> List[str]:
    def dfs(path,ans):
    #Calculate the next number to iterate
        if len(path) == len(digits):
            ans.append(''.join(path))
            return
        
        next_number = int(digits[len(path)])
        for char in cyph[next_number]:
            path.append(char.lower())
            dfs(path,ans)
            path.pop()
        return ans
    return dfs([],[])

letter_combinations_of_phone_number('56')