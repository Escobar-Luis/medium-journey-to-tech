def para (s):
    # Stack to keep track of open paranthesis, how? Well since a stack is LIFO (Last In First Out), we can look at the top of the stack (Stack[-1]) during an iteration where we come across a closing paraenthesis to check that the 'latest' or 'last' open parenthesis we've seen in the string is the same type of open parenthesis to validate it or not. Time complexity for Access, Search, Insertion, or Deletion is linear (O(n))
    stack= []
    #Hash to quickly (O(n) time or linear time) go to a specific type of closing paraenthesis and see it's corresponding closing parenthesis during an iteration where we come across a closing parenthesis and have to compare the actual corresponding open parenthesis to the latest open parentheis we saw in our stack to validate it or not.
    pairs = { ')': '(', '}': '{', ']': '[' }
    for i in range(len(s)):
    # If we come across a closing parenthesis - meaning if the current character in our iteration is a key in our hash where REMEMBER all keys are closing parenthesis
        if s[i] in pairs:
            # If the closing parenthesis we just ran into matches the type of closing parenthesis in our hash as a value pair
            if stack and stack[-1] == pairs[s[i]]:
                # it's a match and we remove the open parenthesis from our stack
                stack.pop()
            # Either:
            # 1) We don't have any value in our stack, so we havent ran into a open parenthesis in a previous iteration, meaning the closed parenthesis we just ran into closes nothing, making it invalid. Or,
            # 2) We have ran into a open parenthesis previously but, it does not match the type of closed parenthesis we just ran into, making it invalid
            else:
                return False
        # We just ran into a open parenthesis
        else:
            # Add it to our stack
            stack.append(s[i])
    # After all iterations, if we have any values in our stack, meaning we have UN-CLOSED open parenthesis, then we return false. If our stack is empty, then all parenthesis have been closed and we do have valid parenthesis!
    return False if stack else True
    
    