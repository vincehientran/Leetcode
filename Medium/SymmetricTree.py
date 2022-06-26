# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.flippedTrees(root.left, root.right)
        else:
            return False


    def flippedTrees(self, tree1, tree2):

        if tree1 == None or tree2 == None:
            return tree1 == tree2
        elif tree1.val == tree2.val:
            return self.flippedTrees(tree1.left, tree2.right) and self.flippedTrees(tree1.right, tree2.left)
        else:
            return False
