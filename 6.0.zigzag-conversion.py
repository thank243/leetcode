"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = list()
        flag = 1
        # 生成空数组
        for _ in range(numRows):
            result += ['']
        # 指标解法
        # for i in range(len(s)):
        #     if i % (numRows - 1) == 0:
        #         start = i
        #     if start % (2*(numRows-1)) == 0:
        #         result[i-start] += s[i]
        #     else:
        #         result[numRows-1-(i-start)] += s[i]
        # return "".join(result)
        i = 0
        for alp in s:
            result[i] += alp
            i += flag
            if i == numRows - 1 or i == 0:
                flag = -flag
        return "".join(result)


print(Solution.convert(Solution, "LEETCODEISHIRING", 4))
