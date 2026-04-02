# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        before_left = dummy
        tail = None
        prev = None
        curr = head
        pos = 1

        while curr:
            if pos >= left and pos <= right:
                if pos == left:
                    tail = curr

                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

                if pos >= right:
                    break
            else:
                if pos < left:
                    before_left = curr

                curr = curr.next
            
            pos += 1

        before_left.next = prev
        tail.next = curr

        # prev = None
        # curr = head
        # # start = None


        # while curr and curr.next:
        #     # if curr.next.val == left:
        #     #     start = curr
        #     if curr.val >= left and curr.val <= right:
        #         next_node = curr.next
        #         curr.next = prev

        #         prev = curr
        #         curr = next_node
        
        # print(prev)
        return dummy.next