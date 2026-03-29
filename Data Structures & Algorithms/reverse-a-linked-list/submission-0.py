# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        if not head:
            return None
        while head.next != None:
            x = head.next
            head.next = prev
            prev = head
            head = x
            print (head.val)
        head.next = prev
        return head