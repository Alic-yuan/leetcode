class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        nh = len(board)
        nl = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        def mark(board, i, j, nh, nl, directions):
            if i < 0 or i > nh - 1 or j < 0 or j > nl - 1 or board[i][j] != 'E':
                return
            min_count = 0
            for x, y in directions:
                if 0 <= i + x <= nh - 1 and 0 <= j + y <= nl - 1 and board[i + x][j + y] == 'M':
                    min_count += 1
            if min_count == 0:
                board[i][j] = 'B'
            else:
                board[i][j] = str(min_count)
                return
            for x, y in directions:
                mark(board, i + x, j + y, nh, nl, directions)

        mark(board, i, j, nh, nl, directions)
        return board
