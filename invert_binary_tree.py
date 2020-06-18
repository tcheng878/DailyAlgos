# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        
        queue = deque()
        queue.append(root)
        head = root
        
        while queue:
            root = queue.pop()
            root.left, root.right = root.right, root.left
            if root.left != None:
                queue.append(root.left)
            if root.right != None:
                queue.append(root.right)
        
        return head