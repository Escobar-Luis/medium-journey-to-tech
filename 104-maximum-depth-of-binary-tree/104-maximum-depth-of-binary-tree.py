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
        def dfs(r):
            if not r:
                return 0

            leftCount = self.maxDepth(r.left) +1
            rightCount = self.maxDepth(r.right) +1

            return max(leftCount,rightCount)
        return dfs(root) 