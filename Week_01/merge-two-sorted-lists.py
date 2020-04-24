# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        cur = res
        p = l1
        l = l2
        while p and l:
            if p.val < l.val:
                res.next = p
                p = p.next
            else:
                res.next = l
                l = l.next
            res = res.next
        res.next = p if p else l
        return cur.next