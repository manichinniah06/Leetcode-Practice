class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return_matrix = [0]*len(matrix)
        for i in range(len(return_matrix)):
            temp = 0
            for j in matrix[i]:
                if j == 1:
                    temp += 1
            return_matrix[i] = temp
        return return_matrix
