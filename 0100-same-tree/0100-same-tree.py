# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same_tree(p, q):
            if not p and not q:
                return True

            if p and q and p.val == q.val:
                return same_tree(p.left, q.left) and same_tree(p.right, q.right)
            else:
                return False 

        return same_tree(p, q)
        