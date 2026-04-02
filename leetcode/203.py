# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        previous = dummy

        while previous.next:
            if previous.next.val == val:
                previous.next = previous.next.next

            else:
                previous = previous.next

        return dummy.next