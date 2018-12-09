'''
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
注意：整数顺序将表示为一个字符串。
'''
'''
超过97.82%
'''
def func(n):
    if n == 1:
        return "1"
    str1 = "1"
    cur = 1
    newstr = ""
    while cur < n :
        b = str1[0]
        c = 0
        newstr = ""
        for i in range(len(str1)):
            if str1[i] == b:
                c += 1
            else:
                newstr = newstr + str(c) + b
                b = str1[i]
                c = 1
            if i == len(str1) - 1:
                newstr = newstr + str(c) + b
        cur += 1
        str1 = newstr
    return newstr

print(func(4))

