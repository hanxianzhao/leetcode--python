'''
递归超过97.66%
迭代超过97.66%
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list1 = []
        def traver(root):
            if root != None:
                traver(root.left)
                list1.append(root.val)
                traver(root.right)
        traver(root)
        return list1

class lteration(object):
    def inorderTraversal(self,root):
        if root == None:
            return []
        list1 = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            list1.append(node.val)
            root = root.right
        return list1