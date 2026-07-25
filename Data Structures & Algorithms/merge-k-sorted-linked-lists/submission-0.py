# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        i = 0
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, i, node))
            i += 1
        head = None
        current = None
        if heap:
            val, list_pos, head = heapq.heappop(heap)
            current = head
            if head.next:
                heapq.heappush(heap, (head.next.val, list_pos, head.next))
        while heap:
            val, list_pos, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, list_pos, node.next))
        if head:
            return head
        return None