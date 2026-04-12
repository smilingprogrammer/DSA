# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        size = 0
        node = head
        
        while node:
            size += 1
            node = node.next

        node = head

        res = []

        base_size, extra = divmod(size, k)

        for _ in range(k):

            dummy = ListNode(-1)
            cur = dummy

            for _ in range(base_size + (extra > 0)):
                cur.next = node
                cur = node
                node = node.next


            if extra > 0:
                extra -= 1

            cur.next = None
            res.append(dummy.next)


        return res