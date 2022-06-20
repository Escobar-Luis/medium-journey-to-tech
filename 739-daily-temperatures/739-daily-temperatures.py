class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)
        
        for i, v in enumerate(temperatures):
            while s and v > s[-1][1]:
                si,sv = s.pop()
                res[si] = i - si
            s.append([i,v])
        return res