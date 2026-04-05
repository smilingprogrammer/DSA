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
        
        if not head:
            return None

        original_to_copy = {}

        dummy = Node(0)

        tail = dummy
        current = head

        while current:
            new_node = Node(current.val)
            tail.next = new_node
            tail = tail.next
            original_to_copy[current] = new_node
            current = current.next

        current = head

        while current:
            if current.random:
                original_to_copy[current].random = original_to_copy[current.random]
            else:
                original_to_copy[current].random = None

            current = current.next

        return dummy.next