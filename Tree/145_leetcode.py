# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#USING TWO STACKS APPROACH (MOST COMMON)

class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        st1=[root]
        st2=[]
        ans=[]
        node=root
        while st1:
            node=st1.pop()
            st2.append(node)
            if node.left:
                st1.append(node.left)
            if node.right:
                st1.append(node.right)
        while st2:
            node=st2.pop()
            ans.append(node.val)
        return ans


