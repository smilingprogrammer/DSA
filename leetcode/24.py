# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        prev = dummy
        curr = head

        while curr and curr.next:

            first = curr
            second = curr.next

            next_pair = second.next

            second.next = first
            first.next = next_pair

            prev.next = second

            prev = first

            curr = next_pair

        if curr:
            prev.next = curr

        return dummy.next