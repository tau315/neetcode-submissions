# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return None
        current = head
        size = 1
        while current.next is not None:
            current = current.next
            size += 1

        
        current = head
        prev = None
        counter = 0
        while counter < (size + 1) // 2:
            prev = current
            current = current.next
            counter += 1

        second_half = current
        prev.next = None        

        # Reverse second half
        current = second_half
        previous = None
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        first_pointer = head
        second_pointer = previous 

        while second_pointer is not None and first_pointer is not None:
            first_next = first_pointer.next
            second_next = second_pointer.next

            first_pointer.next = second_pointer
            second_pointer.next = first_next

            first_pointer = first_next
            second_pointer = second_next

            






