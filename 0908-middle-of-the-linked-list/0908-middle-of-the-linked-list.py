# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nullNode = ListNode()
        nullNode.next = head

        once = nullNode
        twice = nullNode

        while twice:
            once = once.next
            twice = twice.next

            if twice:
                twice = twice.next

        return once