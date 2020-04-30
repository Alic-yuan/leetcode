from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        if n * k == 0:
            return []
        # if k==1:
        #     return nums
        deq = deque()
        def clear_queue(i):
            if deq and deq[0] == i-k:
                deq.popleft()
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
        for i in range(k):
            clear_queue(i)
            deq.append(i)
        res.append(nums[deq[0]])
        for j in range(k,n):
            clear_queue(j)
            deq.append(j)
            res.append(nums[deq[0]])
        return res