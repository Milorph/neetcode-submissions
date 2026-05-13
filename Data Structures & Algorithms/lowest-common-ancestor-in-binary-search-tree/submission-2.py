# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def commonAncestor(root, p, q):

            if root == None:
                return None
            
            
            if root.val > p.val and root.val > q.val:
                return commonAncestor(root.left, p, q)
            elif root.val < p.val and root.val < q.val:
                return commonAncestor(root.right, p, q)
            else:
                return root
        
        return commonAncestor(root, p, q)
            