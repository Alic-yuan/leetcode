# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = ListNode(0)
        cur.next = head
        jump = cur
        k = 0
        p= head
        h = head
        while h:
            h = h.next
            k +=1
            if k % 2 == 0:
                start = p
                end = h
                for _ in range(2):
                    temp = start.next
                    start.next = end
                    end = start
                    start = temp
                jump.next = end
                jump = p
                p = h
        return cur.next

