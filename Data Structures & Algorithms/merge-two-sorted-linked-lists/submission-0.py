# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        h1 = list1
        h2 = list2

        if h1.val<h2.val:
            h=h1
            h1=h1.next
        else:
            h=h2
            h2 = h2.next
        
        x = h
        while h1 and h2:
            if h1.val<h2.val:
                temp = h1
                h1 = h1.next
                temp.next = x.next
                x.next = temp
                x = x.next
            else:
                temp = h2
                h2 = h2.next
                temp.next = x.next
                x.next = temp
                x = x.next
        if h1:
            x.next = h1
        else:
            x.next = h2
        return h
