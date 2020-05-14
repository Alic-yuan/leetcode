from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = defaultdict(list)
        for word in wordList:
            for w in range(len(word)):
                key = word[:w] + '*' + word[w+1:]
                words[key].append(word)
        queue = [(beginWord, 1)]
        visited = set()
        while queue:
            node, level = queue.pop(0)
            # if node == endWord:
            #     return level
            for n in range(len(node)):
                key = node[:n] + '*' + node[n+1:]
                for word in words[key]:
                    if word in visited:
                        continue
                    if word == endWord:
                        return level+1
                    visited.add(word)
                    queue.append((word, level+1))
        return 0