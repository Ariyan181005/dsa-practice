class NumMatrix(object):
    def __init__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        self.p = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                self.p[i+1][j+1] = (matrix[i][j] + self.p[i][j+1] + self.p[i+1][j] - self.p[i][j])

    def sumRegion(self, row1, col1, row2, col2):
        return (self.p[row2+1][col2+1] - self.p[row1][col2+1] - self.p[row2+1][col1] + self.p[row1][col1])
