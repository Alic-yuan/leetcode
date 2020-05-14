class Solution:
    def jump(self, nums: List[int]) -> int:
        max_index = 0
        step = 0
        end = 0
        for i in range(len(nums)-1):
            if max_index >= i:
                max_index = max(max_index, i+nums[i])
            if i==end:
                end = max_index
                step +=1
        return step