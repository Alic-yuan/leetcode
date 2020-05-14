class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        max_index = 0
        for j in range(len(nums)-1):
            if max_index >= j:
                max_index = max(max_index, j+nums[j])
        if max_index >= len(nums)-1:
            return True
        else:
            return False
