#要看单独那个最小的那个recursive单元 别看太大的
#要高清逻辑 我自己现在的
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        #if not root.left or not root.right or root.left.val != root.right.val: return False
        
        def compare(p,q) -> bool:
            if not p.left and q.right: return False
            elif p.left and not q.right: return False
            elif not p.left and not q.right: return True
            
            elif p.left.val != q.right.val: return False
            
            return (compare(p.left,p.right) and compare(p.right,p.left))
        
        #没有renturn！！！
        compare(root.left,root.right)
            
            