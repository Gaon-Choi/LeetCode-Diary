# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        origin = head
        prev_node = head
        next_node = head.next

        while next_node:
            new_node = ListNode()

            new_node.val = gcd(prev_node.val, next_node.val)

            prev_node.next = new_node
            new_node.next = next_node

            prev_node = prev_node.next
            prev_node = prev_node.next

            next_node = next_node.next

        return origin


        