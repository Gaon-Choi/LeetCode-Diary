# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stk = []

        node = head

        while node:
            stk.append(node.val)
            node = node.next

        node = head

        while node:
            if node.val != stk.pop():
                return False
            node = node.next
            
        return True
