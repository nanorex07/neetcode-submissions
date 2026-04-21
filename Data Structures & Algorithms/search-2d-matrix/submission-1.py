class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_index = -1
        l = 0
        h = len(matrix)-1

        while h >= l:
            m = (h+l)//2
            if matrix[m][0] <= target:
                row_index = m
                l = m+1
            else:
                h = m-1
        
        l = 0
        h = len(matrix[row_index])-1
        while h >= l:
            m = (h + l)//2
            if matrix[row_index][m] == target:
                return True
            if matrix[row_index][m] < target:
                l = m+1
            else:
                h = m-1
        
        return False