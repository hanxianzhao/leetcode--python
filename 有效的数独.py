'''
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
说明:
一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
给定数独序列只包含数字 1-9 和字符 '.' 。
给定数独永远是 9x9 形式的。
'''

'''
超过67.96
主要是第三种判断比较难思考
'''
def func(board):
    def compare(nums):
        dict1 = {}
        for i in nums:
            if i in dict1 and i != ".":
                return False
            dict1[i] = i
        return True

    for i in board:
        if not compare(i):
            return False
    for j in range(9):
        list1 = []
        for m in range(9):
            list1.append(board[m][j])
        if not compare(list1):
            return False
    a = [0, 3, 6]
    for k in a:
        for l in a:
            list1 = []
            for i in range(k, k + 3):
                for j in range(l, l + 3):
                    list1.append(board[i][j])
            if not compare(list1):
                return False
    return True
