class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        self.mergesort(nums, 0, len(nums)-1)
        return self.count


    def mergesort(self, nums, left, right):
        if right <= left:
            return
        mid = (left+right) >> 1
        self.mergesort(nums, left, mid)
        self.mergesort(nums, mid+1, right)
        self.merge(nums, left, mid, right)


    def merge(self, nums, left, mid, right):
        temp = []
        i = left
        j = mid+1
        while i<=mid and j <= right:
            if nums[i] > 2*nums[j]:
                self.count += mid-i+1
                j +=1
            else:
                i +=1
        i = left
        j = mid+1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i +=1
            else:
                temp.append(nums[j])
                j +=1
        while i<=mid:
            temp.append(nums[i])
            i +=1
        while j<=right:
            temp.append(nums[j])
            j +=1
        for k in range(len(temp)):
            nums[left+k] = temp[k]