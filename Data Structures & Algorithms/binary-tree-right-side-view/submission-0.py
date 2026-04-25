# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        levelMap = {}

        def preorder(root, level):
            if not root:
                return
            levelMap[level] = root.val
            preorder(root.left, level+1)
            preorder(root.right, level+1)

        preorder(root, 0)
        return [i[1] for i in sorted(levelMap.items())]
            