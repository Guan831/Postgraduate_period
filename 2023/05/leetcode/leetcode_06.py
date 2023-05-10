"""https://leetcode.com/problems/zigzag-conversion/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 当 numRows=1 时，直接返回 s
        if numRows == 1:
            return s

        # 初始化字符串数组 res，用于存储每一行的字符
        res = ['' for _ in range(numRows)]

        # 初始化变量 i 和 flag，其中 i 用于记录当前字符的行数，初始时 i=0，flag=-1，表示方向向上
        i, flag = 0, -1

        # 依次遍历字符串 s 中的每个字符 c，将其加入对应的行 res[i]
        for c in s:
            res[i] += c
            # 如果 i=0 或 i=numRows-1，执行 flag=-flag，表示改变方向
            if i == 0 or i == numRows-1:
                flag = -flag
            # 更新变量 i，如果 flag=1，则 i=i+1，否则 i=i-1
            i += flag

        # 将 res 中的每个元素连接成一个字符串并返回
        return ''.join(res)
