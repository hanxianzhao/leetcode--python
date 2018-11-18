'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
#判断一下当左边的括号大于右边的括号数量时即可添加右边的括号
#左边括号添加的数量不能大于总个数
def func(n):
    result = []
    def add(s = "",left = 0,right = 0):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left<n:
            add(s+"(",left+1,right)
        if right<left:
            add(s+")",left,right+1)
    add()
    return result

if __name__ == '__main__':
    print(func(3))