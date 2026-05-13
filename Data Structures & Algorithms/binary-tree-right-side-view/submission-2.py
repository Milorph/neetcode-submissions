# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = deque()
        res = []

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
            res.append(tmpList[-1])
        

        return res
        