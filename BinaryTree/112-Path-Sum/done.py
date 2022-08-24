# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root,res):
            # basic situation
            if not root: return False
            # 先加起来 这样好算一点
            res += root.val
        
            if not root.left and not root.right:
                return res == targetSum
            
            return dfs(root.left,res) or dfs(root.right,res)
        
        # res = 0
        # dfs(root,res)
        return dfs(root,0)
            

            
        