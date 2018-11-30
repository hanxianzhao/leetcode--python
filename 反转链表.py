'''
反转一个单链表。
示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''
'''
普通循环86.77%
递归62.84%
相比较简单的题目递归相对较慢
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 直接循环赋值
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur != None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    #递归解法
    def recursive(self,head):
        if head.next == None:
            return head
        if head.next != None:
            a = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return a

