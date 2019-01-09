'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:
1 ≤ m ≤ n ≤ 链表长度。
示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
'''

def func(head,m,n):
    a = 1
    cur = head
    prev = None
    if m == 1:
        pass
    else:
        while True:
            if a+1 == m:
                cur1 = cur
            if a == m:
                cur2 = cur
            if a >= m:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            if a == n:
                cur2.next = cur
                cur1.next = prev
                break
            a += 1
        return head