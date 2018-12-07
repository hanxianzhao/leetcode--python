'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        cur = l3
        while l1 != None or l2 != None:
            if l1 == None:
                if l2.val >= 10:
                    l3.next = ListNode(l2.val - 10)
                    l3.next.next = ListNode(1)
                else:
                    l3.next = l2
                break
            if l2 == None:
                if l1.val >= 10:
                    l3.next = ListNode(l1.val - 10)
                    l3.next.next = ListNode(1)
                else:
                    l3.next = l1
                break
            
            a = l1.val + l2.val
            if a >= 10:
                a = a - 10
                if l1.next != None:
                    l1.next.val += 1
                elif l2.next != None:
                    l2.next.val += 1
                else:
                    l3.next = ListNode(a)
                    l3.next.next = ListNode(1)
                    break
            l3.next = ListNode(a)
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        return cur.next
