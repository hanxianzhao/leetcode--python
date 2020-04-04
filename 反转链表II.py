'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:
1 ≤ m ≤ n ≤ 链表长度。
示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
'''
class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def func(head,m,n):
    a = 1
    ret = head
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
            print(a)
        print("23")
        return ret

a = Node(3)
b = Node(4)
c = Node(5)
d = Node(6)
e = Node(7)
a.next = b
b.next = c
c.next = d
d.next = e


ret = func(a,2,4)
list1 = []
print("fuck")
while ret != None:
    print(ret.val)
    list1.append(ret.val)
    ret = ret.next

print(list1)