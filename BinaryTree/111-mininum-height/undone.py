# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # recursive一直不停找下去，iterative找到一个就可以啦
        # 要看root是不是为null
        if not root: return 0
        q = deque([root])
        level = 1
        
        while q:
            # 足有两个点都检查一遍才能进入下一层
            for i in range(len(q)):
                if not q[i].left and not q[i].right:
                    return level
                
            node = q.popleft()
            # 这里有一个错误的点看了左边没有看到邮编 如果左边多了一层 就直接加一层 明显是不对的
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

            level +=1
        
        return level
                
                
'''Input
[0,2,4,1,null,3,-1,5,1,null,6,null,8]
Output
5
Expected
4
'''