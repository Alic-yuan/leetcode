class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            temp ="".join(sorted(i))
            if temp not in dic:
                dic[temp] = [i]
            else:
                dic[temp].append(i)
        return list(dic.values())