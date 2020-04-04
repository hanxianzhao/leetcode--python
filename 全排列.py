'''
给定一个没有重复数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
[1,2,3,4]
[
    [1,2,3,4]
    [1,2,4,3]
    [1,3,2,4]
    [1,3,4,2]
    [1,4,3,2]
    [1,4,2,3]
]
'''
'''
超过95.17%
'''
def func(nums):
    if (len(nums) <= 1):
        return [nums]
    r = []
    for i in range(len(nums)):
        #
        s = nums[:i] + nums[i + 1:]
        p = func(s)
        for x in p:
            r.append(nums[i:i + 1] + x)
    return r

print(func([1,2,3]))