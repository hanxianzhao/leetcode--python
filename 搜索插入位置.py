'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
示例 1:
输入: [1,3,5,6], 5
输出: 2
示例 2:
输入: [1,3,5,6], 2
输出: 1
示例 3:
输入: [1,3,5,6], 7
输出: 4
示例 4:
输入: [1,3,5,6], 0
输出: 0
'''
'''
执行用时: 44 ms, 在Search Insert Position的Python3提交中击败了99.16% 的用户
简单的二分查找
'''
def func(nums,target):
    #二分查找
    left = 0
    right = len(nums) - 1
    mid = 0
    while left <= right:
        mid = int((left + right) / 2)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return left

print(func([1,3,5,6],0))