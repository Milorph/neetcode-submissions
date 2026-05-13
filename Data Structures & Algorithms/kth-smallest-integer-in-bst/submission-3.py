# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = k
        num = None

        def inorder(root):
            nonlocal count, num

            if root == None:
                return None
            
            inorder(root.left)
            count -= 1
            if count == 0:
                num = root.val
                return
            inorder(root.right)
        
        inorder(root)
        return num

        