# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        goodCount = self.dfs(root, float('-inf'))
        
        return goodCount
        
    def dfs(self, node, largest):
        goodCount = 0
        
        if node.val >= largest:
            goodCount += 1
        newLargest = max(node.val, largest)
            
        if node.left:
            goodCount += self.dfs(node.left, newLargest)
        if node.right:
            goodCount += self.dfs(node.right, newLargest)
            
        return goodCount