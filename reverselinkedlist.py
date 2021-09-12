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
            
        