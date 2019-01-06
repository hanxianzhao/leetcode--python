'''
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1
'''
def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(needle) == 0:
        return 0
    cur = len(needle)
    if len(needle) == 1:
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1
    for i in range(len(haystack)):
        if len(haystack) < i + cur:
            return -1
        if haystack[i] == needle[0]:
                if haystack[i:i+cur] == needle:
                    return i