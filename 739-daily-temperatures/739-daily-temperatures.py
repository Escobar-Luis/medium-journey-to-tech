class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r = [0] * len(temperatures)
        s = []
        
        for i,v in enumerate(temperatures):
            while s and v > s[-1][0]:
                t, si = s.pop()
                r[si] = i-si
            s.append([v,i])
        return r