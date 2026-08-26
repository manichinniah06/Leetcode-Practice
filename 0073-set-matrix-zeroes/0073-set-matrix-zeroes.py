class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zero_count = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_count.append((i,j))
        
        for i,j in zero_count:
            for col in range(len(matrix[i])):
                matrix[i][col] = 0
            
            for row in range(len(matrix)):
                matrix[row][j] = 0
        