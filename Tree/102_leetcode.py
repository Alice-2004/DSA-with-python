# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    
    def levelOrder(self, root):
        if not root:
            return []
        q=[]
        ans=[]
        q.append(root)
        cur=0
        while q:
            ans.append([])
            for i in range(len(q)):
                node=q.pop(0)
                ans[cur].append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            cur+=1
        
        return ans


        
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        