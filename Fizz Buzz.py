'''
写一个程序，输出从 1 到 n 数字的字符串表示。
1. 如果 n 是3的倍数，输出“Fizz”；
2. 如果 n 是5的倍数，输出“Buzz”；
3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
'''
'''
超过99.38%
'''
def func(n):
    if n == 0:
        return []
    list1 = []
    for i in range(1,n+1):
        if i % 3 == 0:
            if i % 5 == 0:
                list1.append("FizzBuzz")
                continue
            list1.append("Fizz")
            continue
        if i % 5 == 0:
            list1.append("Buzz")
            continue
        list1.append(str(i))
    return list1