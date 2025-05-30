# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        lst=[]
        
        if not root:
            return lst
        s=[]
        s=[(root,str(root.val))]
        while s:
            node,path=s.pop()
            if not node.left and not node.right:
                lst.append(path)
            if node.right:
                s.append((node.right,path + "->" + str(node.right.val)))
            if node.left:
                s.append((node.left,path + "->" + str(node.left.val)))

            
        return lst

        