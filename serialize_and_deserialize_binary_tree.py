# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output = ""
        queue = deque([root])
        while queue and queue.count(None) != len(queue):
            curroot = queue.popleft()
            if curroot == None:
                output += "None,"
                queue.append(None)
                queue.append(None)
            else:
                output = output + str(curroot.val) + ","
                queue.append(curroot.left)
                queue.append(curroot.right)
        return output
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        data.pop(-1)
        
        head = TreeNode(data.pop(0))
        queue = [head]
        while(len(data) > 0):
            curhead = queue.pop(0)
            popleft = data.pop(0)
            popright = data.pop(0)
            if popleft == "None":
                curhead.left = TreeNode(null)
            else:
                curhead.left = TreeNode()
                
            if popright == "None":
                curhead.right = TreeNode(null)
            else:
                curhead.right = TreeNode()                                 
            queue.append(curhead.left)
            queue.append(curhead.right)
            
        return head

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))