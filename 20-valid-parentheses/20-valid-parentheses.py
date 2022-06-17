class Solution:
    def isValid(self, s: str) -> bool:
        h = {')': '(', ']':'[','}':'{'}
        stack = []
        for c in s:
            if c in h:
                if not stack or stack[-1] != h[c]:
                    print(c)
                    print(stack)
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack