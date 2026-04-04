# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        fast = slow = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
            
            # curr = curr.next
            # head = head.next

            # if curr.next is None and dummy.next == curr.next:
            #     return True

        return False