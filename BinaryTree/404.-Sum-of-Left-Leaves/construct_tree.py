class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = [3,9,20,None,None,15,7]

def cons(lst):
    for i in range(0,len(lst)-1,3):
        TreeNode(val = lst[i],left=TreeNode(lst[]))
