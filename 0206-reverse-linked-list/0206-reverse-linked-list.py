# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_ll = ListNode()

        while head != None:
            node = ListNode(val = head.val)
            header = reversed_ll.next
            
            node.next = header
            reversed_ll.next = node

            head = head.next

        return reversed_ll.next


        