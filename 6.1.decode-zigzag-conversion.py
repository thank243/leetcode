"""
反解Z字变换
"""


class Solution(object):
    def decode(self, s, numRows):
        row_list = []
        mapping = dict()
        # 生成空数组和空字典
        for _ in range(numRows):
            row_list += [0]
            mapping.setdefault(_, 0)
        # 确定每行字符数
        flag = 1
        i = 0
        for _ in s:
            row_list[i] += 1
            i += flag
            if i == numRows - 1 or i == 0:
                flag = -flag
        # 将Z字变换后的字符串按行排列
        i = 0
        str_list = []
        for num in row_list:
            str_list.extend([s[i:num + i]])
            i += num
        # 按数组提取字符
        i = 0
        decode = str()
        flag = 1
        for _ in s:
            decode += str_list[i][mapping[i]]
            mapping[i] += 1
            i += flag
            if i == numRows - 1 or i == 0:
                flag = -flag
        return decode


print(Solution.decode(Solution, "LCIRETOESIIGEDHN", 3))
