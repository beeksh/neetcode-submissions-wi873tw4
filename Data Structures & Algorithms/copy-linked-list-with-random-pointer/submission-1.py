"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        x = head
        d = {None: None}
        dummy = Node(0)
        curr = dummy
        while x:
            new = Node(x.val)
            d[x]=new
            curr.next = new
            curr = curr.next
            x = x.next # xxx
            
        x = head
        curr = dummy.next
        while x:
            curr.random = d[x.random]
            curr=curr.next
            x = x.next
        return dummy.next
