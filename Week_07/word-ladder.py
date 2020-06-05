from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # words = defaultdict(list)
        # for word in wordList:
        #     for i,j in enumerate(word):
        #         key = word[:i] + '*' + word[i+1:]
        #         words[key].append(word)
        # queue = [(beginWord, 1)]
        # visit = set()
        # while queue:
        #     node, level = queue.pop(0)
        #     if node == endWord:
        #         return level
        #     for i,j in enumerate(node):
        #         key = node[:i] + '*' + node[i+1:]
        #         for k in words[key]:
        #             if k in visit:
        #                 continue
        #             visit.add(k)
        #             queue.append((k, level+1))
        # return 0
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        queue = [(beginWord, 1)]
        visit = set()
        while queue:
            node, step = queue.pop(0)
            if node == endWord:
                return step
            for i in range(len(node)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if j != node[i]:
                        new_node = node[:i] + j + node[i + 1:]
                        if new_node in visit:
                            continue
                        if new_node in wordList:
                            visit.add(new_node)
                            wordList.remove(new_node)
                            queue.append((new_node, step + 1))
        return 0
        # if endWord not in wordList:
        #     return 0
        # front = {beginWord}
        # back = {endWord}
        # step = 1
        # wordList = set(wordList)
        # L = len(beginWord)

        # while front:
        #     step+=1
        #     nextf = set()
        #     for word in front:
        #         for i in range(L):
        #             for c in string.ascii_lowercase:
        #                 if c!=word[i]:
        #                     new_word = word[:i]+c+word[i+1:]
        #                     if new_word in back:
        #                         return step
        #                     if new_word in wordList:
        #                         nextf.add(new_word)
        #                         wordList.remove(new_word)
        #     front = nextf
        #     if len(back)<len(front):
        #         back,front=front,back
        # return 0