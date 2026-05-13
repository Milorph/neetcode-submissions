# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque()
        if root:
            queue.append(root)
        res = []

        def bfs(root, q):
            nonlocal res
        
            while q:
                temp_arr = []
                for i in range(len(q)):
                    node = q.popleft()
                    if node:
                        temp_arr.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.append(temp_arr)
            
        bfs(root, queue)

        return res



