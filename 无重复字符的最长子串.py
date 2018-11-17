'''b
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "acabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''
def func(s):
    if s == "":
        return 0
    i = 0
    dict1 = {}
    list1 = []
    for j in range(len(s)):
        if s[j] not in dict1:
            dict1[s[j]] = j
            if j == len(s)-1:
                list1.append(j-i+1)
        else:
            list1.append(j-i)
            m = dict1[s[j]]
            for key in s[i:dict1[s[j]]+1]:
                dict1.pop(key)
            dict1[s[j]] = j
            i = m + 1
    return max(list1)

if __name__ == '__main__':
    ss = "pwwkew"
    print(func(ss))