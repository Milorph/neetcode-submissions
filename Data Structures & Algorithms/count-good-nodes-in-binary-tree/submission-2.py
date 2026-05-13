# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        goods = 0

        def dfs(root, rootVal):
            nonlocal goods

            if root == None:
                return None

            if root.val >= rootVal:
                print(root.val)
                goods += 1
                rootVal = max(rootVal, root.val)
            dfs(root.left, rootVal)
            dfs(root.right, rootVal)
        
        dfs(root, float('-inf'))

        return goods
