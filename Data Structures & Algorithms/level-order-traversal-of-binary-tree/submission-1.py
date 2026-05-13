# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = []

        q = deque()

        if root:
            q.append(root)

        while q:
            tmpList = []
            
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    tmpList.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            levels.append(tmpList)

        return levels

