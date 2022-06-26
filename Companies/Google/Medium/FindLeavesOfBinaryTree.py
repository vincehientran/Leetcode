# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.output = []
    
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.getHeight(root)
        
        return self.output
        
    def getHeight(self, node):
        
        if node == None:
            return -1
        
        heightLeft = self.getHeight(node.left)
        heightRight = self.getHeight(node.right)
        
        height = max(heightLeft, heightRight) + 1
        
        if len(self.output) <= height:
            self.output.append([node.val])
        else:
            self.output[height].append(node.val)
        
        return height