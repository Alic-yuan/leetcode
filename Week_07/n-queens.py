class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.cols = set()
        self.pie = set()
        self.na = set()
        self.dfs(0, n, [])
        res = self.process_result(n)
        return res

    def dfs(self, depth, n, cur):
        if depth == n:
            self.result.append(cur)
            return

        for col in range(n):
            if col in self.cols or col+depth in self.pie or col-depth in self.na:
                continue
            self.cols.add(col)
            self.pie.add(col+depth)
            self.na.add(col-depth)

            self.dfs(depth+1,n,cur+[col])

            self.cols.remove(col)
            self.pie.remove(col+depth)
            self.na.remove(col-depth)

    def process_result(self,n):
        res = []
        for i in self.result:
            temp = []
            for j in i:
                temp2 = '.'*(j) + 'Q' + '.'*(n-j-1)
                temp.append(temp2)
            res.append(temp)
        return res