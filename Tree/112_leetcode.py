# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def path_sum(root,cur_sum):
            if not root:
                return False
            cur_sum+=root.val

            if not root.left and not root.right:
                if cur_sum==targetSum:
                    return True
                else:
                    return False
            return path_sum(root.left,cur_sum) or path_sum(root.right,cur_sum)
        return path_sum(root,0)
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        