'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
示例 1:
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
'''
'''
巨特码难想，搜了一下别人做的学习下
超过62.05%
'''
def func(nums):
    a = len(nums)
    if a == 0:
        return 0
    if a == 1:
        return nums[0]
    if a == 2:
        return max(nums[0],nums[1])
    res = []
    res.append(nums[0])
    res.append(max(nums[0],nums[1]))
    for i in range(2,a):
        res.append(max(res[i-1],res[i-2]+nums[i]))
    return res[a-1]

print(func([1,2,3,1]))

'''
大神代码
'''
def func1(nums):
    last, now = 0, 0
    for n in nums:
        last, now = now, max(last + n, now)
    return max(last, now)