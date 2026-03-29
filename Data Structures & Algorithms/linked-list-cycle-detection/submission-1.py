# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        n, m = head, head
        if not head:
            return False
        while m.next and m.next.next:
            n = n.next
            m = m.next.next
            if n==m:
                return True
        return False