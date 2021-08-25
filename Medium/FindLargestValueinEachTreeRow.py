# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        ret = [root.val]
        queue = [root.left, root.right]

        while queue:
            layer = []

            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    layer.append(node.val)
                    queue += [node.left] + [node.right]

            if len(layer) > 0:
                ret.append(max(layer))

        return ret
                
