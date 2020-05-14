class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        i = 0
        j = 0
        for bill in bills:
            if bill == 5:
                i +=1
            elif bill == 10:
                if i == 0:
                    return False
                else:
                    i -=1
                    j +=1
            else:
                if i == 0:
                    return False
                else:
                    if j ==0 and i <3:
                        return False
                    elif j == 0 and i >=3:
                        i -=3
                    else:
                        i -=1
                        j -=1
        return True