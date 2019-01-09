'''
超过100%
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root == None:
            return
        list1 = []
        node = root
        a = 0
        while node or list1:
            while node:
                list1.append(node)
                node = node.left
            node = list1.pop()
            a += 1
            if a == k:
                return node.val
            node = node.right