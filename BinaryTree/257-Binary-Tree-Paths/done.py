# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]: 
                
        def dfs(root,path):
            path += str(root.val)
            if not root.left and not root.right: return res.append(path)

            if root.left:
                dfs(root.left, path + '->')

            if root.right:
                dfs(root.right, path + '->')
                
        res = []
        #path = list(root.val)
        path= ''
        if not root: return None
        dfs(root,path)
        return res

            