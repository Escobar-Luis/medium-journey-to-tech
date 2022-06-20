class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def recurse(o,c):
            if o == c == n:
                res.append(''.join(stack))
                return
            if o< n:
                stack.append('(')
                recurse(o+1,c)
                stack.pop()
            if c<o:
                stack.append(')')
                recurse(o,c+1)
                stack.pop()
        
        recurse(0,0)
        return res