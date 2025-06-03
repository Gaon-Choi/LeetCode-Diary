# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stk = []

        node = head

        # 링크드리스트를 순회하며 차례대로 스택에 넣음
        while node:
            stk.append(node.val)
            node = node.next

        node = head

        # 링크드리스트를 다시 순회하며 스택의 top과 비교
        while node:
            if node.val != stk.pop():
                return False
            node = node.next
            
        return True
