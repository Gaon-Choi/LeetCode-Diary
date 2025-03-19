# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(tree):
            if not tree:
                return 0

            left, right = dfs(tree.left), dfs(tree.right)

            if left == -1:
                return -1

            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1
        
            return max(left, right) + 1

        return dfs(root) != -1