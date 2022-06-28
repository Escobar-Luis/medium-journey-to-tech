class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position,speed)]
        
        stack = []
        for p,s in reversed(sorted(pairs)):
            time = (target-p) /s
            stack.append(time)
            while len(stack)>1 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)