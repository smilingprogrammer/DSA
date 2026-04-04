# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode(0, None)

        l1_str1 = ""
        l2_str2 = ""
        current = l1
        prev = None
        while current:
            l1_str1 += str(current.val)
            current = current.next
        
        current2 = l2
        prev2 = None
        while current2:
            l2_str2 += str(current2.val)
            current2 = current2.next

        result = int(l1_str1[::-1]) + int(l2_str2[::-1])

        tail = dummy
        for char in str(result)[::-1]:
            new_node = ListNode(int(char))
            tail.next = new_node
            
            tail = tail.next

        return dummy.next