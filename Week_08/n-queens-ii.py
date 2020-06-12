class Solution:
    def totalNQueens(self, n: int) -> int:
        if n<1:
            return
        self.count = 0
        self.dfs(n,0,0,0,0)
        return self.count

    def dfs(self, n, depth, cols, pie, na):
        if depth == n:
            self.count +=1
            return

        state = (~(cols|pie|na)) & ((1 << n) -1)

        while state:
            p = state & (-state)
            state = state & (state-1)
            self.dfs(n, depth+1, cols|p, (pie|p) << 1, (na|p) >> 1)