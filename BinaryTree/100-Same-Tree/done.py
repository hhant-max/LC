# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        # 本题中止的条件 一个有一个没有 自然 就种植条件啦
        # 或者是返过来？ 怎么简便的写？
        if not p or not q or p.val != q.val: return False
             
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right))

        