class Solution:
    def jump(self, nums: List[int]) -> int:
        max_index = 0
        count = 0
        end = 0
        for i in range(len(nums) - 1):
            max_index = max(max_index, i + nums[i])
            if i == end:
                count += 1
                end = max_index
        return count