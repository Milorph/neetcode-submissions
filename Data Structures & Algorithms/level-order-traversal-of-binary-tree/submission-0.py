# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        d = deque()
        if root:
            d.append(root)

        
        while d:
            tmpList = []

            for i in range(len(d)):
                node = d.popleft()
                tmpList.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            res.append(tmpList)
        
        return res
                    

               


        