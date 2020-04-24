class Solution:
    def trap(self, height: List[int]) -> int:
        temp = 0
        left = 0
        high = 1
        right = len(height)-1
        while left <= right:
            while left<=right and height[left] < high:
                left +=1
            while right>=left and height[right] < high:
                right -=1
            temp += right-left+1
            high +=1
        area = sum(height)
        return temp-area