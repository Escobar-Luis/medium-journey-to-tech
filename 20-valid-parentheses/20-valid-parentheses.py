class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        h = {')':'(','}':'{',']':'['}
        for b in s:
            if b in h:
                if stack and h[b] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return True if not stack else False