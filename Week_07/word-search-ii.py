class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for w in word:
                node = node.setdefault(w,{})
            node['#'] = '#'
        res = []

        def dfs(cur, i, j, trie, board):
            temp = board[i][j]
            if temp not in trie:
                return
            trie = trie[temp]
            if '#' in trie and trie['#'] == '#':
                res.append(cur+temp)
                trie['#'] = 0
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            board[i][j] = 0
            for x,y in directions:
                nx = i+x
                ny = j+y
                if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny] !=0:
                    dfs(cur+temp,nx,ny,trie,board)
            board[i][j] = temp


        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs('',i,j,trie,board)

        return res
