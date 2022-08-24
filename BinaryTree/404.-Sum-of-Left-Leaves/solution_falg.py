class Solution(object):
    def sumOfLeftLeaves(self, root):
        self.sum = 0
        def function(root,x):
            if not root.left and not root.right:
                if x == 'left':
                    self.sum += root.val
            if root.left:
                function(root.left, "left")
            if root.right:
                function(root.right, "right")
        
        function(root, "")
        return self.sum