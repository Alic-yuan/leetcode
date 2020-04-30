class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []
        check_state = [0 for i in range(len(nums))]
        self.helper(0, nums, [],check_state)
        return self.result

    def helper(self, depth, nums, cur_state,check_state):
        if depth==len(nums):
            self.result.append(cur_state[:])
            return
        for i in range(len(nums)):
            if check_state[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i-1] and check_state[i-1]==0:
                continue
            check_state[i] = 1
            cur_state.append(nums[i])
            self.helper(depth+1,nums,cur_state, check_state)
            cur_state.pop()
            check_state[i] = 0