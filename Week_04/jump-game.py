class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for i in range(len(nums) - 1):
            if max_index >= i:
                max_index = max(max_index, i + nums[i])
        return max_index >= len(nums) - 1
