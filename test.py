# def MergeSort(lists):
#     if len(lists) <= 1:
#         return lists
#     num = int( len(lists) / 2 )
#     left = MergeSort(lists[:num])
#     right = MergeSort(lists[num:])
#     print(left,right)
#     return Merge(left, right)
# def Merge(left,right):
#     r, l=0, 0
#     result=[]
#     while l<len(left) and r<len(right):
#         if left[l] < right[r]:
#             result.append(left[l])
#             l += 1
#         else:
#             result.append(right[r])
#             r += 1
#     result += list(left[l:])
#     result += list(right[r:])
#     return result
# print(MergeSort([1, 2, 3, 4, 5, 6, 7, 90, 21, 23, 45]))

# a = 1
# b = None
# print(a > b)
# # print(c)
# a = 10
# b = a**0.5
# print(b)

class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

a = Node(3)
a.next = Node(2)
list1 = []
while a != None:
    list1.append(a.val)
    a = a.next
print(list1)