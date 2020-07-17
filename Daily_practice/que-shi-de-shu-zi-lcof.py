class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == mid:
                left +=1
            else:
                right -=1
        return left