class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nh = len(board)
        nl = len(board[0])
        hang = [set() for _ in range(nh)]
        lie = [set() for _ in range(nl)]
        block = [set() for _ in range(nh)]
        for i in range(nh):
            for j in range(nl):
                block_index = (i//3)*3 + j//3
                if board[i][j] != '.':
                    if board[i][j] not in hang[i]:
                        hang[i].add(board[i][j])
                    else:
                        return False
                    if board[i][j] not in lie[j]:
                        lie[j].add(board[i][j])
                    else:
                        return False
                    if board[i][j] not in block[block_index]:
                        block[block_index].add(board[i][j])
                    else:
                        return False
        return True