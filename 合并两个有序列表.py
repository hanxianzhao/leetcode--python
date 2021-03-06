'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def func(l1,l2):
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if l1.val < l2.val:
        cur = l1
        l1 = l1.next
    else:
        cur = l2
        l2 = l2.next
    result = cur
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1 == None:
        cur .next = l2
    else:
        cur.next = l1
    return result



