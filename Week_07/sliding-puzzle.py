class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        board = tuple(board[0] + board[1])
        queue = [(board, 0)]
        visited = set()
        while queue:
            node, step = queue.pop(0)
            if node == (1, 2, 3, 4, 5, 0):
                return step
            index = node.index(0)
            for i in moves[index]:
                node2 = list(node)
                node2[i], node2[index] = node2[index], node2[i]
                node3 = tuple(node2)
                if node3 in visited:
                    continue
                visited.add(node3)
                queue.append((node3, step+1))
        return -1