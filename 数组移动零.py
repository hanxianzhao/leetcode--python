'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
'''
'''
超过94.75%
'''

def func(nums):
    if nums == []:
        return []
    cur = 0
    a = 0
    b = len(nums)
    while cur + a < b:
        if nums[cur] == 0:
            nums.pop(cur)
            a += 1
            nums.append(0)
        else:
            cur += 1
    return nums

print(func([0,1,0,3,12]))
