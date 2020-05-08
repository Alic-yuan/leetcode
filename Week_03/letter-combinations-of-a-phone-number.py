class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {'2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'}
        res = []
        def helper(string,digits):
            if len(digits) == 0:
                res.append(string)
                return
            letter = digits[0]
            letters = dic[letter]
            for l in letters:
                helper(string+l, digits[1:])
        helper('', digits)
        return res