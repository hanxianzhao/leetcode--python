'''
请判断一个链表是否为回文链表。
示例 1:
输入: 1->2
输出: false
示例 2:
输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''
'''
反转链表超过62.16%
直接使用列表比较超过79.61%

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #使用O(n)复杂度来求解，反转后比对即可
    #空间复杂度多使用了一个列表（其实没必要反转链表，取出对应的值在列表中直接比较即可）
    #O(1)空间复杂度使用快慢指针，找到中间节点反转后面的节点然后两个链表进行比较
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        1 2 3 4 5 6
        """
        list1 = []
        cur = head
        prev = None
        while head != None:
            list1.append(head.val)
            head = head.next
        while cur != None:
            a = cur.next
            cur.next = prev
            prev = cur
            cur = a
        b = 0
        while prev != None:
            if prev.val != list1[b]:
                return False
            prev = prev.next
            b += 1
        return True

    def func(self,head):
        list1 = []
        while head != None:
            list1.append(head.val)
            head = head.next
        a = 0
        b = len(list1) -1
        while a <= b-1:
            if list1[a] != list1[b]:
                return False
            a += 1
            b -= 1
        return True