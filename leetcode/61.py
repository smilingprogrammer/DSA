# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return None

        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        k = k % length

        if k == 0:
            return head
        
        # curr = head
        # prev = None

        new_tail = head

        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        tail.next = head


        # while curr is not None:

        #     nextNode = curr.next
        #     curr.next = prev

        #     prev = curr

        #     curr = nextNode

        # i = 0
        # curr = None
        # while i < k:
        #     dummy = ListNode(prev.val, curr)
        #     prev = prev.next

        #     tail = dummy
        #     while tail.next and tail.next.next:
        #         tail = tail.next

        #     tail.next = None

        #     curr = dummy

        #     i += 1

        return new_head