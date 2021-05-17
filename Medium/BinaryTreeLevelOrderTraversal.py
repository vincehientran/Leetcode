# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        if not root:
            return result

        queue = [root]

        # BFS
        while queue:
            currentLevel = []
            for _ in range(len(queue)):
                node = queue.pop(0)

                if node:
                    currentLevel.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if len(currentLevel) != 0:
                result.append(currentLevel)

        return result
