# Valid Parentheses: A string has valid parentheses if each bracket is closed and opened in the same order and has the same type.
# Idea: Since stack is LIFO, we look at the top of the stack to check the 'latest' parentheses. During each iteration, if the character is an opening paranthesis, we push it onto the stack. If the character is a closing parenthesis, we look at the top of stack to see if there is a corresponding open parenthesis, if they dont, then we found a non-match pair and return false
# Time Complexity: O(n), where n is the size of the strings.
# Space Complexity:
# Stability:
def valid_parentheses(s: str) -> bool:
    # stack going to keep track opening parenthesis
    stack = []
    # dict with closing parenthesis as keys and their values are corresponding opening parenthesis
    pairs = { ')': '(', '}': '{', ']': '[' }
    # iterating through every character of given string
    for c in s:
        # if c is a closing parenthesis
        if c in pairs: 
            if stack and stack[-1] == pairs[c]: # a matching brackets exists at top of the stack
                stack.pop()
            else:
                return False
        else: # c is an opening parenthesis, push onto the stack (first iteration)
            stack.append(c)
    print( False if stack else True)

valid_parentheses("([][]{}){}{")