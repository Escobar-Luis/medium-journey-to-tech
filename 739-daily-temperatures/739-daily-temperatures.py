class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []
        
        for i,t in enumerate(temperatures):
            while s and t > s[-1][1]:
                si,st = s.pop()
                res[si] = (i - si)
            s.append([i,t])
        return res