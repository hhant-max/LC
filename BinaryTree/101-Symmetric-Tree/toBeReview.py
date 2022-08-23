# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
                
        return self.compare(root.left,root.right)
        
        #if not root.left or not root.right or root.left.val != root.right.val: return False
        
    def compare(self, p,q) -> bool:
        if not p and q: return False
        elif p and not q: return False
        elif not p and not q: return True

        elif p.val != q.val: return False

        return (self.compare(p.left,q.right) and self.compare(p.right,q.left))


