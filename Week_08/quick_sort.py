def quick_sort(nums, left, right):
    if left >= right:
        return
    p = pivation(nums, left, right)
    quick_sort(nums, left, p-1)
    quick_sort(nums, p+1, right)

def pivation(nums, left, right):
    mark = left
    p = nums[left]
    for i in range(left+1, right+1):
        if nums[i] < p:
            mark +=1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[mark], nums[left] = nums[left], nums[mark]
    return mark


nums = list([3,5,8,1,5,10,6])
quick_sort(nums, 0, len(nums)-1)
print(nums)
