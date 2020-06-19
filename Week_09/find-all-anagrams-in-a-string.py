class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        window = {}
        seeds = {}
        for i in p:
            seeds[i] = seeds.get(i, 0) +1

        length = len(p)
        limit = len(s)
        left = right = 0

        while right <limit:
            if s[right] not in seeds:
                window.clear()
                left = right = right+1
            else:
                window[s[right]] = window.get(s[right], 0) + 1
                if right-left+1 == length:
                    if window==seeds:
                        res.append(left)
                    window[s[left]] -= 1
                    left +=1
                right +=1
        return res