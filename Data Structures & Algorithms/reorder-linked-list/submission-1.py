# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        while head:
            nodes.append(head)
            head=head.next
        print(nodes)
        l, r = 0, len(nodes)-1

        dummy = ListNode()
        curr = dummy
        while l<r:
            curr.next = nodes[l]
            curr = curr.next
            curr.next = nodes[r]
            curr = curr.next
            l+=1
            r-=1
        if l==r:
            curr.next = nodes[l]
            curr = curr.next
        curr.next = None
        head = dummy.next