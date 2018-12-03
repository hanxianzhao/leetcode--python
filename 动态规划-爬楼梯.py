'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''
'''
被提示过 是一个斐波拉契数列
func使用递归直接超时
func1超过99.36%
'''
def func(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return  func(n-1) + func(n-2)

def func1(n):
    a = 1
    b = 1
    cur = 1
    while cur < n:
        c = b
        b = a + b
        a = c
        cur += 1
    return b
print(func1(4))



print(func(4))