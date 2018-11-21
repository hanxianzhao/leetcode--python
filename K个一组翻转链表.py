'''
给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。
示例 :
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5
说明 :
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''
'''
执行用时: 68 ms, 在Reverse Nodes in k-Group的Python3提交中击败了98.79% 的用户
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        prev = None
        cur = head
        next = None
        check = head
        n = 0
        count = 0
        while n < k and check != None:
            check = check.next
            n += 1
        if n == k:
            while count < k and cur != None:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
                count += 1
            if next != None:
                head.next = self.reverseKGroup(next, k)
            return prev
        else:
            return head