# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None or head.next.next is None:
            return False
        slower = head.next
        faster = head.next.next
        while slower.next is not None and faster.next is not None and faster.next.next is not None:
            if slower == faster:
                return True
            slower = slower.next
            faster = faster.next.next
        return False