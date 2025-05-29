# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        def same(p,q):
            if (not p and not q):
                return True
            if (not p or not q):
                return False
            if (p.val != q.val):
                return False
            left=same(p.left,q.left)
            right=same(p.right,q.right)
            if left and right:
                return True
            else:
                return False
        def has_sub(root):
            if not root:
                return False
            if same(root,subRoot):
                return True
            return has_sub(root.left) or has_sub(root.right)        
        return has_sub(root)    
            
            
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        