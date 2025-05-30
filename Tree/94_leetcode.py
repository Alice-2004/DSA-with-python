# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        stack=[]
        ans=[]
        node=root
        while node or stack:
            while node:
                stack.append(node)
                node=node.left
            node=stack.pop()
            ans.append(node.val)
            node=node.right
        return ans
        

       
        