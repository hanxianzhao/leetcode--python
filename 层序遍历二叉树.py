'''
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
'''
'''
超过70.25%
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        list2 = []
        list2.append([root.val])
        list3 = [root]
        while True:
            if list3:
                list4 = []
                list1 = []
                for i in list3:
                    if i.left:
                        list4.append(i.left)
                        list1.append(i.left.val)
                    if i.right:
                        list4.append(i.right)
                        list1.append(i.right.val)
                list3 = list4
                list2.append(list1)
            else:
                break
        return list2[:-1]