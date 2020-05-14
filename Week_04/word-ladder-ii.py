from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for word in wordList:
            for w in range(len(word)):
                key = word[:w] + '*' + word[w+1:]
                words[key].append(word)
        pre_words = defaultdict(list)
        queue = [(beginWord, 1)]
        be_found = {beginWord:1}
        while queue:
            node, level = queue.pop(0)
            for n in range(len(node)):
                key = node[:n] + '*' + node[n+1:]
                for word in words[key]:
                    if word not in be_found:
                        be_found[word] = level+1
                        queue.append((word, level+1))
                    if be_found[word] == level+1:
                        pre_words[word].append(node)
            if endWord in be_found and level+1 > be_found[endWord]:
                break
        res = []
        def helper(cur,beginWord, endWord, pre_words, length):
            if len(cur) == length:
                res.append(cur[::-1])
                return
            for word in pre_words[endWord]:
                helper(cur+[word], beginWord, word, pre_words, length)
        if endWord in be_found:
            length = be_found[endWord]
            helper([endWord], beginWord, endWord, pre_words, length)
            return res
        else:
            return []