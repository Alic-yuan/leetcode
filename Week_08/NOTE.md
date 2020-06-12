学习笔记

## 实战位运算要点
    1、判断奇偶:
        x%2==1 -> (x&1)==1
        x%2==1 -> (x&1)==0
    2、x//2 -> x>>1
    3、x=x&(x-1) -> 清零最低位的1
    4、x=x&-x -> 得到最低位的1
    5、x&~x -> 0
    
## 布隆过滤器 VS Hash table
    Hash table 不仅可以判断元素是否在集合中，还能得到其存储的信息
    布隆只可以判断是否在集合中
    
## 布隆
    优点是空间效率和查询时间效率都远远超过一般的算法
    缺点是有一定的误识别率和删除困难
    
## 排序算法

### 冒泡排序
    def bubble_sort(array):
        for i in range(len(array)-1):
            for j in range(len(array)-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]

### 插入排序
    def insertion_sort(array):
        if len(array) <= 1: return
    
        for i in range(1, len(array)):
            value = array[i]
            j = i - 1
            while j >= 0 and array[j] > value:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = value
 
### 选择排序
    def selection_sort(array):
        if len(array) <= 1: return
    
        for i in range(len(array)):
            min_index = i
            min_val = array[i]
            for j in range(i, len(array)):
                if array[j] < min_val:
                    min_val = array[j]
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]
            
### 快速排序
    def quick_sort(begin, end, nums):
        if begin >= end:
            return
        pivot_index = partition(begin, end, nums)
        quick_sort(begin, pivot_index-1, nums)
        quick_sort(pivot_index+1, end, nums)

    def partition(begin, end, nums):
        pivot = nums[begin]
        mark = begin
        for i in range(begin+1, end+1):
            if nums[i] < pivot:
                mark +=1
                nums[mark], nums[i] = nums[i], nums[mark]
        nums[begin], nums[mark] = nums[mark], nums[begin]
        return mark
        
### 归并排序
    def mergesort(nums, left, right):
        if left >= right:
            return
        mid = (left+right) >> 1
        mergesort(nums, left, mid)
        mergesort(nums, mid+1, right)
        merge(nums, left, mid, right)

    def merge(nums, left, mid, right):
        temp = []
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
        nums[left:right+1] = temp
        
### 堆排序
    def heapify(parent_index, length, nums):
        temp = nums[parent_index]
        child_index = 2*parent_index+1
        while child_index < length:
            if child_index+1 < length and nums[child_index+1] > nums[child_index]:
                child_index = child_index+1
            if temp > nums[child_index]:
                break
            nums[parent_index] = nums[child_index]
            parent_index = child_index
            child_index = 2*parent_index + 1
        nums[parent_index] = temp

    def heapsort(nums):
        for i in range((len(nums)-2)//2, -1, -1):
            heapify(i, len(nums), nums)
        for j in range(len(nums)-1, 0, -1):
            nums[j], nums[0] = nums[0], nums[j]
            heapify(0, j, nums)    