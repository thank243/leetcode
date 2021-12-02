"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution:
    def reverse(self, x: int) -> int:
        str_num = str(x)
        flag = 1
        if not str_num[0].isnumeric():
            flag = -1
            str_num = str_num[1:]
        result = ""
        i = 1
        for _ in str_num:
            result += str_num[-i]
            i += 1
        output = int(result) * flag
        if output > 2 ** 31 - 1 or output < -2 ** 31:
            return 0
        return output
