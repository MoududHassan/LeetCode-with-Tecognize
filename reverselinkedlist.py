# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        run = head
        stack = []
        while run:
            stack.append(run)
            run = run.next
        newhead = None
        run1 = None
        while stack:
            temp = stack.pop()
            if not newhead:
                newhead = temp
                run1 = temp
            else:
                run1.next=temp
                run1 = run1.next
            if len(stack) == 0:
                run1.next = None
        return newhead

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        prev = None
        while head:
            temp = ListNode(head.val,head.next)
            temp.next = prev
            prev = temp
            head = head.next
        return temp
    
    
        def recu(self, head:Optional[ListNode], prev:Optional[ListNode]):
            if not head:
                return prev
            temp = head.next
            head.next = prev
            prev = head
            return recu(self, temp, prev)
        result = recu(self,head, None)
        return result
