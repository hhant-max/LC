# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
       # 答题思路是要进行recursive res 在外面所以 可以下面创建一个函数内的函数
        def traverse(node):
            if node == None: return 0
            
            res.append(node.val)
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        
        return res
        

                
            
        