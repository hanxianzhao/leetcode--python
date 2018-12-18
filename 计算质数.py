'''
统计所有小于非负整数 n 的质数的数量。
示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''

def func(n):
    if n == 0 or n== 1 or n==2:
        return 0
    if n == 3:
        return 1
    result = 1
    for i in range(3,n):
        for j in range(2,i//2+2):
            if i%j == 0:
                break
            if j == i//3+1:
                result +=1
                break
    return result

print(func(499979))