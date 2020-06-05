class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nh = len(board)
        nl = len(board[0])
        hang = [set() for _ in range(nh)]
        lie = [set() for _ in range(nl)]
        blocks = [set() for _ in range(9)]

        empty = []

        for i in range(nh):
            for j in range(nl):
                block_index = (i//3)*3+(j//3)
                if board[i][j] == '.':
                    empty.append((i,j))
                else:
                    hang[i].add(int(board[i][j]))
                    lie[j].add(int(board[i][j]))
                    blocks[block_index].add(int(board[i][j]))

        def dfs(depth):
            if depth==len(empty):
                return True
            i,j = empty[depth]
            block_index = (i//3)*3+(j//3)
            for k in range(1,10):
                if k in hang[i] or k in lie[j] or k in blocks[block_index]:
                    continue
                hang[i].add(k)
                lie[j].add(k)
                blocks[block_index].add(k)

                board[i][j] = str(k)

                if dfs(depth+1):
                    return True

                hang[i].remove(k)
                lie[j].remove(k)
                blocks[block_index].remove(k)
            return False

        dfs(0)
