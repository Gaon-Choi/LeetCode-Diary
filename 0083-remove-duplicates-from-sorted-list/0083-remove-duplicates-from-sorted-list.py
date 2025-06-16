# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = head
        first = head
        second = head

        while second:
            if first.val == second.val:
                second = second.next
            else:
                first.next = second
                first = first.next

        if first:
            first.next = None

        return ans