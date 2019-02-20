'''
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。
说明：一个单词是指由字母组成，但不包含任何空格的字符串。
示例:
输入: "Hello World"
输出: 5
'''

def func(s):
    s = s.strip()
    list1 = s.split(" ")
    if len(list1) == 0:
        return 0
    else:
        return len(list1[-1])



print(func("a"))

s = "11111 "
s = s.strip()
print(s)