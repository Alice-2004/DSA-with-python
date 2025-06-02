# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        min_d=[float('inf')]
        prev=[None]
        stack=[]
        node=root
        while node or stack:
            while node:
                stack.append(node)
                node=node.left
            node=stack.pop()
            if prev[0] is not None:
                min_d[0]=min(min_d[0],node.val-prev[0])
            prev[0]=node.val
            node=node.right
        return min_d[0]

        
    
       
        # Time: O(n)
        # Space: O(n)

                
        