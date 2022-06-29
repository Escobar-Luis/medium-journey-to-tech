class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        
        top,bot = 0, rows-1
        
        while top<=bot:
            m = (top + bot) //2
            if matrix[m][-1] < target:
                top = m+1
            elif matrix[m][0] > target:
                bot = m-1
            else:
                break
        
        mid = (top + bot)//2
        l,r = 0, len(matrix[mid])-1
        while l<=r:
            m = (l+r)//2
            if matrix[mid][m] < target:
                l = m+1
            elif matrix[mid][m]> target:
                r = m-1
            else:
                return True
        
        return False