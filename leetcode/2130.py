# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = fast = head
        # current = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        maximum = 0
        first = head
        second = prev

        while second:
            maximum = max(maximum, first.val + second.val)
            first = first.next
            second = second.next
            
        return maximum