# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        lst = self.orderedList(root)
        return lst[k-1]

    def orderedList(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # if the node is None, then just return empty List
        if root == None:
            return []
        else:
            return self.orderedList(root.left) + [root.val] + self.orderedList(root.right)
