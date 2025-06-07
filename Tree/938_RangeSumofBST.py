class Solution(object):
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0
        
        
        if low <= root.val <= high:
            return (root.val +
                    self.rangeSumBST(root.left, low, high) +
                    self.rangeSumBST(root.right, low, high))
        
       
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
     
        else:
            return self.rangeSumBST(root.left, low, high)