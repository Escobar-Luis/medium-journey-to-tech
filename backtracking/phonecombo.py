from typing import List
# Given a phone number that contains 2-9, find all possible letter combinations the phone number could translate to.

KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}
    # I am going to have to have two states:
    # The path of the leters to add to my result
    # Keep track of the letters I have already used
def letter_combinations_of_phone_number(digits: str) -> List[str]:
    def dfs(path, res):
        # We append the permutation to our result once the length of our path(combo) is equal to the length of digits
        if len(path) == len(digits):
            res.append(''.join(path))
            return
        # Because digits string is 0 indexed, we can use the length of our path to calculate next number since lengths are 1-indexed.
        next_number = digits[len(path)]
        # We are using the next number to acess our dictionary for the letters we are able to use
        for letter in KEYBOARD[next_number]:
            # We are appending the letter to our path
            path.append(letter)
            # passing that letter as the new state in our recursive call
            dfs(path, res)
            # Once we hit our base case, our path (combo of letters) is finished so we pop it of 
            path.pop()

    res = []
    dfs([], res)
    return res
def letter_combinations_of_phone_number(digits: str) -> List[str]:

    def dfs(path,used,result):
        if len(digits)==len(result):
            result.append(''.join(path))
            return
        for i,digit in enumerate(digits):
            if used[i]:
                continue
            path.append(digit)
            used[i]=True
            dfs(path,used,result)
            path.pop()
            used[i]=False
    res=[]
    return dfs([],[False]*len(digits),res)