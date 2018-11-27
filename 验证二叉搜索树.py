'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:
输入:
    2
   / \
  1   3
输出: true
示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
'''
'''
超过74.29%
使用中序遍历 得到的列表为递增的
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        list1 = []
        def recurse(node):
            if node != None:
                recurse(node.left)
                list1.append(node.val)
                recurse(node.right)
        recurse(root)
        for i in range(len(list1)):
            if i == 0:
                continue
            if list1[i] <= list1[i-1]:
                return False
        return True

