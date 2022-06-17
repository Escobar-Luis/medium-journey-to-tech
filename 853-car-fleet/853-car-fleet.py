class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position, speed)]
        
        stack = []
        for p,s in sorted(pairs)[::-1]:
#         appending time to stack
            stack.append((target-p)/s)
#           if we have more than 2 cars in stack and if the time we just appended is less than the previous time than we know they will collide and form a fleet so we pop from our stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)