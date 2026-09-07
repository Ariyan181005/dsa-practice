class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        r = len(board)
        c = len(board[0])
        o = [row[:] for row in board]
        for i in range(r):
            for j in range(c):
                cnt = 0
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if x == i and y == j:
                            continue
                        if 0 <= x < r and 0 <= y < c:
                            cnt += o[x][y]
                if o[i][j] == 1:
                    if cnt < 2 or cnt > 3:
                        board[i][j] = 0
                else:
                    if cnt == 3:
                        board[i][j] = 1