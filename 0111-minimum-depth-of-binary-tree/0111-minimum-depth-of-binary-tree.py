# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = 1e9

        stack = [(root, 1)]

        while stack:
            tr, depth = stack.pop()

            if tr is None:
                continue

            if (tr.left is None) and (tr.right is None):
                min_depth = min(min_depth, depth)
                continue

            if tr.left is not None:
                stack.append((tr.left, depth + 1))
            
            if tr.right is not None:
                stack.append((tr.right, depth + 1))

        if min_depth == 1e9:
            return 0
            
        return min_depth        