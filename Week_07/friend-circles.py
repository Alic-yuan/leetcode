class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        father = [i for i in range(len(M))]

        def find(a):
            if father[a] != a:
                father[a] = find(father[a])
            return father[a]

        def union(a, b):
            father[find(b)] = find(a)
            return find(a)

        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j]:
                    union(i, j)

        for k in range(len(M)):
            find(k)

        return len(set(father))

        # def dfs(i,visited):
        #     visited[i]=1
        #     for j in range(len(M)):
        #         if visited[j]==0 and M[i][j]==1:
        #             dfs(j,visited)

        # visited = [0]*len(M)
        # ans = 0
        # for i in range(len(M)):
        #     if visited[i] == 0:
        #         dfs(i,visited)
        #         ans+=1
        # return ans