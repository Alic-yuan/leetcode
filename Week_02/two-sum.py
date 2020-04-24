class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        n = len(nums)
        res = []
        for i in range(n):
            if target - nums[i] not in dic:
                dic[nums[i]] = i
            else:
                res.append(dic[target-nums[i]])
                res.append(i)
        return res