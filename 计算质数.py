'''
统计所有小于非负整数 n 的质数的数量。
示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''
'''
太特么难了，根本过不了测试
'''
def func(n):
    if n == 0 or n== 1 or n==2:
        return 0
    if n == 3:
        return 1
    list1 = [2,3]
    result = 1
    for i in range(3,n):
        if i%2 == 0 or i % 3 == 0:
            continue
        cur = i ** 0.5
        for j in list1:
            if j > cur:
                list1.append(i)
                break
            if i%j == 0:
                break
    return len(list1)

print(func(2))
# print(func(499979))
print(func(999983))

print("test")