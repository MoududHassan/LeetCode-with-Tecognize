# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nhead, h1, h2 = None, l1, l2
        runner = None
        c = 0
        while h1 and h2:
            s = h1.val + h2.val + c
            c = int(s / 10)
            s = s % 10
            temp = ListNode(s)
            if not nhead:
                nhead = temp
                runner = temp
            else:
                runner.next = temp
                runner = temp
            h1 = h1.next
            h2 = h2.next
        while h1:
            s = h1.val + c
            c = int(s / 10)
            s = s % 10
            runner.next = ListNode(s)
            runner = runner.next
            h1 = h1.next
            
        while h2:
            s = h2.val + c
            c = int(s / 10)
            s = s % 10
            runner.next = ListNode(s)
            runner = runner.next
            h2 = h2.next
        if c != 0:
            runner.next = ListNode(c)
            runner = runner.next
        return nhead
        