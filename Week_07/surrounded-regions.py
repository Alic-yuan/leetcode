class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board

        def dfs(i, j, board):
            board[i][j] = 'B'
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in directions:
                nx = i + x
                ny = j + y
                if 1 <= nx < len(board) and 1 <= ny < len(board[0]) and board[nx][ny] == 'O':
                    dfs(nx, ny, board)

        for i in range(len(board)):
            if board[i][0] == 'O':
                dfs(i, 0, board)
            if board[i][len(board[0]) - 1] == 'O':
                dfs(i, len(board[0]) - 1, board)

        for j in range(len(board[0])):
            if board[0][j] == 'O':
                dfs(0, j, board)
            if board[len(board) - 1][j] == 'O':
                dfs(len(board) - 1, j, board)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = 'O'