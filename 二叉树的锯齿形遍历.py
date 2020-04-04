'''
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：
[
  [3],
  [20,9],
  [15,7]
]
'''
'''
超过41.09%
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        result = []
        ele = []
        list1 = [root]
        list2 = []
        a = 2
        while list1 or list2:
            if a % 2 == 0:
                ele = []
                for i in list1:
                    ele.append(i.val)
                result.append(ele)
                list2 = []
                for i in range(len(list1)):
                    node = list1.pop()
                    if node.right:
                        list2.append(node.right)
                    if node.left:
                        list2.append(node.left)
                a += 1
            else:
                ele = []
                for i in list2:
                    ele.append(i.val)
                result.append(ele)
                list1 = []
                for i in range(len(list2)):
                    node = list2.pop()
                    if node.left:
                        list1.append(node.left)
                    if node.right:
                        list1.append(node.right)
                a += 1
        return result