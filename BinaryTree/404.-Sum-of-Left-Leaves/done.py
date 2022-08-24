# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        
        def sumLeft(root) ->int:
            #if not root: return 0
            #if not root.left and not root.right: return 0

            if root.left and not root.left.left and not root.left.right: 
                self.res += root.left.val
            
            if root.left:
                sumLeft(root.left)
                
            if root.right:
                sumLeft(root.right)
        
        sumLeft(root)
        return self.res

        
        