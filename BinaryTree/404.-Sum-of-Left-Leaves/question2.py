from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 只是0， 问题再这个局部变量上
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def sumLeft(root, res) ->int:
            #if not root: return 0
            #if not root.left and not root.right: return 0

            if root.left and not root.left.left and not root.left.right: 
                res += root.left.val
            
            if root.left:
                sumLeft(root.left,res)
                
            if root.right:
                sumLeft(root.right,res)
            return res
        
        res = 0
        res = sumLeft(root,res)
        return res

        
#res = Solution().sumOfLeftLeaves(root = [3,9,20,None,None,15,7])
#print(res)