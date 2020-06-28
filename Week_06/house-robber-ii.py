class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <2:
            return nums[0]
        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)
        dp1[0] = nums[0]
        dp2[0] = 0
        for i in range(1, len(nums)):
            if i==1:
                dp1[i] = dp1[i-1]
            elif i==len(nums)-1:
                dp1[i] = dp1[i-1]
            else:
                dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])
        return max(dp1[-1], dp2[-1])