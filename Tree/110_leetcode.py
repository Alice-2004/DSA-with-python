# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        balanced=[True]
        def depth(root):
            if not root:
                return 0

            left_sub_depth=depth(root.left)
            if balanced[0] is False:
                return 0

            right_sub_depth=depth(root.right)
            if abs(left_sub_depth - right_sub_depth) > 1:
                balanced[0]=False
                return 0
            
            return 1 + max(left_sub_depth,right_sub_depth)

        depth(root)
        return balanced[0]

        #TC - O(n)
        #SC - O(h)    


        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        