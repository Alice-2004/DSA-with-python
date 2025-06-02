# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        lca = [root]

        def search(root):
            if not root:
                return

            lca[0] = root
            if root is p or root is q:
                return
            elif root.val < p.val and root.val < q.val:
                search(root.right)
            elif root.val > p.val and root.val > q.val:
                search(root.left)
            else:
                return

        search(root)
        return lca[0]

# Time Complexity: O(h) { here "h" is the height of the binary search tree }
# Space Complexity: O(h) { here "h" is the height of the binary search tree }

                