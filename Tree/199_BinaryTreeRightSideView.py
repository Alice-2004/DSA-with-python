# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        t=self.LevelOrder(root)
        return [i[-1] for i in t]


    def LevelOrder(self,root):
        if not root:
            return None
        q=[]
        q.append(root)
        ans=[]
        level=0
        while q:
            ans.append([])
            for i in range(len(q)):
                node=q.pop(0)
                ans[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1

        return ans
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        