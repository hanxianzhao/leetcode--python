'''
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
'''
'''
执行用时: 28 ms, 在Merge Sorted Array的Python提交中击败了99.56% 的用户
'''
def  func(nums1, m, nums2, n):
    cur = 0
    cur2 = 0
    while cur2 < len(nums2):
        print(cur,m+cur2)
        if cur == m + cur2:
            nums1.insert(m+cur2,nums2[cur2])
            nums1.pop()
            cur2 += 1
            continue
        if nums2[cur2] <= nums1[cur]:
            nums1.insert(cur,nums2[cur2])
            nums1.pop()
            cur2 += 1
        cur += 1
    return nums1

print(func([1,5,9,0,0,0,0,0,0],3,[2,3,6,10,11,12],3))