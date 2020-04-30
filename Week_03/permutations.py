class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        check = [0 for i in range(len(nums))]
        self.helper(0, [], nums, check)
        return self.result

    def helper(self, depth, sol, nums, check):
        if depth == len(nums):
            self.result.append(sol[:])
            return
        for i in range(len(nums)):
            if check[i] == 1:
                continue
            check[i] = 1
            sol.append(nums[i])
            self.helper(depth+1,sol,nums, check)
            sol.pop()
            check[i] = 0