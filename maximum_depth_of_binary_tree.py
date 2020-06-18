# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        def recurse(root, depth):
            right = left = 0
            depth += 1
            if root.left == None and root.right == None:
                return depth
            if root.left != None:
                left = recurse(root.left, depth)
            if root.right != None:
                right = recurse(root.right, depth)
            if left > right and left > depth:
                return left
            elif right >= left and right > depth:
                return right
            else:
                return depth
            
        return recurse(root, 0)