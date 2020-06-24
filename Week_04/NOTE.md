学习笔记

## DFS代码-递归写法
    visited = set()
    def dfs(node,visited):
        if node in visited:
            return
        visited,add(node)
        for next_node in node.children():
           if not next_node in visited:
               dfs(next_node,visited)
               
## 贪心算法与动态规划的区别
    贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。
    动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

## 二分查找的前提
    1、目标函数单调性（单调递增或者递减）
    2、存在上下界
    3、能够通过索引访问
    
## 二分查找模板
    left,right = 0,len(array)-1
    while left <= right:
        mid = (left+right)//2
        if array[mid]==target:
            break or return result
        elif array[mid] < target:
            left = mid+1
        else:
            right = mid-1
            
## 使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[left]