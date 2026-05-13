# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(tree1, tree2):
            if (tree1 == None and tree2 == None):
                return True
            
            if tree1 and tree2 and tree1.val == tree2.val:
                
                return sameTree(tree1.left, tree2.left) and sameTree(tree1.right, tree2.right)
            return False

        def dfs(root, subRoot):

            if root == None:
                return False
        
            
            return sameTree(root, subRoot) or dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        return dfs(root,subRoot)
                
