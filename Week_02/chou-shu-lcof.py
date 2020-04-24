class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n==0:
            return
        if n==1:
            return 1
        nums = [1]
        i,j,k=0,0,0
        for h in range(n-1):
            temp = min(2*nums[i],3*nums[j],5*nums[k])
            if temp == 2*nums[i]:
                i+=1
            if temp == 3*nums[j]:
                j+=1
            if temp == 5*nums[k]:
                k+=1
            nums.append(temp)
        return nums[-1]