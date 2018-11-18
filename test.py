class Solution:
    def swapPairs(self, head):
        if head == None:
            return None
        else:
            r1 = head
            r2 = head
            r2 = r2.next
            result = r2
        if r2 == None:
            return head
        else:
            while r1.next.next != None:
                mdi1 = r1.next.next
                mdi2 = r2.next.next
                r2.next = r1
                if mdi2 == None:
                    r1.next = mdi1
                    return result
                else:
                    r1.next = mdi2
                    r1 = mdi1
                    r2 = mdi2
                    r2.next = r1
                    r1.next = None
                    return result

if head == None:
    return head
cur = ListNode(0)
cur.next = head
first =cur
while cur.next and cur.next.next:
    n1 = cur.next
    n2 = n1.next
    nxt = n2.next
    n1.next = nxt
    n2.next = n1
    cur.next = n2
    cur = n1
return first.next