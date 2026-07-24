# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        current = head
        size = 1
        while current.next is not None:
            size += 1
            current = current.next
        current = head
        if size == n:
            return current.next
        counter = 0
        previous = None
        while counter < size - n:
            previous = current
            current = current.next
            counter += 1
        next_node = current.next
        previous.next = next_node
        return head