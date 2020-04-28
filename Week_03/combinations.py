class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.reslut = []
        self.col = set()
        self.helper(0, k, n, [],1)
        return self.reslut

    def helper(self, depth, k, n, cur_state, first):
        if depth == k:
            self.reslut.append(cur_state[:])
            return
        for i in range(first,n+1):
            cur_state.append(i)
            self.helper(depth+1,k,n,cur_state,i+1)
            cur_state.pop()