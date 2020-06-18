class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        lis = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    lis.append([row, col])
                    
        for i in range(len(lis)):
            for j in range(len(matrix)):
                matrix[j][lis[i][1]] = 0
            for j in range(len(matrix[0])):
                matrix[lis[i][0]][j] = 0