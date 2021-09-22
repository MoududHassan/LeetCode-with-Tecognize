# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        result = None
        temp = result
        while h1 and h2:
            if h1.val >= h2.val:
                if result == None:
                    result = ListNode(h2.val, h2.next)
                    temp = result
                    h2 = h2.next
                else:
                    temp.next = h2
                    h2 = h2.next
                    temp = temp.next
            else:
                if result == None:
                    result = ListNode(h1.val, h1.next)
                    temp = result
                    h1 = h1.next
                else:
                    temp.next = h1
                    h1 = h1.next
                    temp = temp.next
        
        if h1:
            if temp == None:
                result = ListNode(0)
                result = h1
            else:
                temp.next = h1
        if h2:
            if temp == None:
                result = ListNode(0)
                result = h2
            else:
                temp.next = h2
        return result