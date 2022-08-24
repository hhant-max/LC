# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        
        def dfs(root,res):
            if not root.left and not root.right and (res + root.val) == targetSum: return True

            if root.left:
                res += root.left.val
                dfs(root.left,res)

            if root.right:
                res += root.right.val
                dfs(root.right,res)
                
            return 0
        
        res = root.val
        dfs(root,res)
        # stilll incorrect
            

            
        