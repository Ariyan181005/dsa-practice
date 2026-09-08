class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        self.p = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                self.p[i+1][j+1] = (matrix[i][j] + self.p[i][j+1] + self.p[i+1][j] - self.p[i][j])

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return (self.p[row2+1][col2+1] - self.p[row1][col2+1] - self.p[row2+1][col1] + self.p[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)