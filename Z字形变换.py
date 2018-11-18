'''
将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：

P   A   H   N
A P L S I I G
Y   I   R
之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"

实现一个将字符串进行指定行数变换的函数:

string convert(string s, int numRows);
示例 1:

输入: s = "PAYPALISHIRING", numRows = 3
输出: "PAHNAPLSIIGYIR"
示例 2:

输入: s = "PAYPALISHIRING", numRows = 4
输出: "PINALSIGYAHRPI"
解释:
P A Y P A L I S H I  R  I  N  G
0 1 2 3 4 5 6 7 8 9 10 11 12 13
1 2 3 4 3 2 1 2 3 4 3  2  1  2

P     I    N
A   L S  I G
Y A   H R
P     I
'''
'''
首先要找到每一行各字符之间的关系
比如第二行对应的下标分别为 1  5  7  11  13
第三行则为 2  4  8  10  14
可以归纳总结出对应的两个公式：较远的为(numRows-1)*2 - 2(i-1) = 2numRows - 2i
较近的为：2 * ( i - 1 ) = 2i - 2
当为第一行的时候较近的公式为0 判断后进行跳过
当为最大一行时较远的公式为0 判断后进行跳过
使用while循环进行不断地叠加，当最后叠加出来的字符串长度大于len（s）时结束
'''
def func(s,numRows):
    if numRows <= 1 or len(s) <= numRows:
        return s
    result = ""
    lens = len(s) - 1
    for i in range(1,numRows+1):
        far = 2 * numRows - 2 * i
        low = 2 * i - 2
        cur = i - 1
        result += s[cur]
        while cur <= lens:
            if far != 0:
                cur += far
                if cur <= lens:
                    result += s[cur]
            if low != 0:
                cur += low
                if cur <= lens:
                    result += s[cur]
    return result

if __name__ == '__main__':
    s = "dfghjkl"
    print(func(s,1))


