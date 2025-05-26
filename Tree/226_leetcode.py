# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
#TC -O(n) where n are number of nodes
#SC -O(h) 
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        