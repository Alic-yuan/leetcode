class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        if length * k == 0:
            return []
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] +=1
        lis = list(dic.items())
        def down_adjust(parent_index,length,array=[]):
            temp = array[parent_index]
            child_index = 2*parent_index+1
            while child_index<length:
                if child_index+1 < length and array[child_index+1][1]<array[child_index][1]:
                    child_index +=1
                if temp[1] <= array[child_index][1]:
                    break
                array[parent_index] = array[child_index]
                parent_index = child_index
                child_index = 2*parent_index+1
            array[parent_index] = temp
        def up_adjust(child_index, array=[]):
            temp = array[child_index]
            parent_index = (child_index-1)//2
            while parent_index>0:
                if temp[1] >= array[parent_index][1]:
                    break
                array[child_index] = array[parent_index]
                child_index = parent_index
                parent_index = (child_index-1)//2
            array[child_index] = temp
        arr1 = lis[:k]
        for i in range((len(arr1)-2)//2,-1,-1):
            down_adjust(i,len(arr1),arr1)
        arr2 = lis[k:]
        for j in arr2:
            if j[1] <= arr1[0][1]:
                continue
            else:
                arr1[0] = j
                down_adjust(0,len(arr1),arr1)
        res = []
        for h in arr1:
            res.append(h[0])
        return res