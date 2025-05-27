# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        max_diameter=[0]
        def height(root):
            if not root:
                return 0
            left_sub_height=height(root.left)
            right_sub_height=height(root.right)

            diameter=left_sub_height+right_sub_height

            max_diameter[0]=max(max_diameter[0],diameter)

            return 1 + max(left_sub_height,right_sub_height)

        height(root)
        return max_diameter[0]
    
    #time-O(n)
    #space-O(h)
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        