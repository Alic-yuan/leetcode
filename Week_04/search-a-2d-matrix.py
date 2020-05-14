class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        temp = []
        for i in matrix:
            temp = temp + i
        left = 0
        right = len(temp)-1
        while left <= right:
            mid = (left+right)//2
            if temp[mid] == target:
                return True
            elif temp[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return False