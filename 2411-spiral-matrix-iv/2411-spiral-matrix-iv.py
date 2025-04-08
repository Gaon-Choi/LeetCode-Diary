# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]

        i, j = 0, 0
        dxs = [0, 1, 0, -1]
        dys = [1, 0, -1, 0]
        d = 0

        while head:
            matrix[i][j] = head.val

            if not (0 <= i + dxs[d] < m and 0 <= j + dys[d] < n and matrix[i + dxs[d]][j + dys[d]] == -1):
                d = (d + 1) % 4

            i += dxs[d]
            j += dys[d]

            head = head.next

        return matrix