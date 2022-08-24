# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        stack = deque([root])
        if not stack: return 0
        
        while stack:
            track = []
            for _ in range(len(stack)):
                node = stack.popleft()
                track.append(node.val)
                if node.left:
                    stack.append(node.left.val)
                if node.right:
                    stack.append(node.right.val)
        return track[0]
            
        