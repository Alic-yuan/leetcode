class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i,j in enumerate(s):
            if j not in dic:
                dic[j] = i
            else:
                dic[j] = -1
        min_index = float('inf')
        for item in dic.items():
            if item[1] == -1:
                continue
            min_index = min(item[1], min_index)

        return min_index if min_index != float('inf') else -1