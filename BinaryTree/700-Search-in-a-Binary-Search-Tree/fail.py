# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 问题出在如果 左边返回了该有的值 你还进入到下一层循环到右边去 最后就会返回None
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return None
        if root.val == val:
            return root
        
        self.searchBST(root.left if root.left else None,val)
        self.searchBST(root.right if root.right else None,val)
        
        return root if root else None