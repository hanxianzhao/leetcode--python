'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。
进阶：
你能尝试使用一趟扫描实现吗？
'''

#解法为两次遍历链表
#查看其遍历一次链表的过程并没有什么意义，只是多加了一个指针使其中间的间隔为n
#移动的时候还是移动的两个指针与遍历两次链表没有什么区别

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
        cur = head
        a = 1
        while cur.next != None:
            a += 1
            cur = cur.next
        b = a - n
        cur = head
        c = 1
        if b == 0:
            return head.next
        while c != b:
            cur = cur.next
            c += 1
        cur.next = cur.next.next
        return head

