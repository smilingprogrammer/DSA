# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        left = ListNode()
        right = ListNode()

        tleft, tright = left, right

        while head:
            if head.val < x:
                tleft.next = head
                tleft = tleft.next
            
            else:
                tright.next = head
                tright = tright.next

            head = head.next

        tright.next = None
        tleft.next = right.next

        return left.next