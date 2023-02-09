'''
https://leetcode.cn/problems/zigzag-conversion/
6. N 字形变换
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);


示例 1：

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
示例 3：

输入：s = "A", numRows = 1
输出："A"


提示：

1 <= s.length <= 1000
s 由英文字母（小写和大写）、',' 和 '.' 组成
1 <= numRows <= 1000
'''
import math


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        s_list = [x for x in s]
        print(s_list)
        result = list()
        n = len(s)
        numColumns = math.floor(n / numRows)
        index = 0
        for j in range(numColumns):
            for i in range(numRows):
                print(index)
                if index < n:
                    print(s_list[index])
                    result[j][i] = s_list[index]
                    index+=1
                else:
                    break


        for i in result:
            print(i)



    def convert1(self, s: str, numRows: int) -> str:
        '''
        利用二维矩阵模拟
        t:O(r*n)
        s:O(r*n)
        :param s:
        :param numRows:
        :return:
        '''
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s
        t = r * 2 - 2
        c = (n + t - 1) // t * (r - 1)
        mat = [[''] * c for _ in range(r)]
        x, y = 0, 0
        for i, ch in enumerate(s):
            mat[x][y] = ch
            if i % t < r - 1:
                x += 1 #向下移动
            else:
                x -= 1
                y += 1 # 向右上移动
        return ''.join(ch for row in mat for ch in row if ch)


    def convert2(self, s:str, numRows:int) -> str:
        '''
        t:O(n)
        s:O(n)
        压缩矩阵空间
        :param s:
        :param numRows:
        :return:
        '''
        r = numRows
        if r == 1 or r >= len(s):
            return s
        mat = [[] for _ in range(r)]
        t, x = r * 2 - 2, 0
        for i, ch in enumerate(s):
            mat[x].append(ch)
            x += 1 if i % t < r - 1 else -1
        return ''.join(chain(*mat))

    def convert3(self, s:str, numRows:int)->str:
        '''
        直接构造
        t: O(n)
        s: O(1)
        :param s:
        :param numRows:
        :return:
        '''
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s
        t = r * 2 - 2
        ans = []
        for i in range(r): # 枚举矩阵的行
            for j in range(0, n - i, t): # 枚举每个周期的起始下标
                ans.append(s[j + i]) # 当前周期的第一个字符
                if 0 < i < r - 1 and j + t - i < n:
                    ans.append(s[j + t - i]) # 当前周期的第二个字符
        return ''.join(ans)


if __name__ == "__main__":
    solution = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    result = "PAHNAPLSIIGYIR"

    s = "PAYPALISHIRING"
    numRows = 4
    result = "PINALSIGYAHRPI"

    # s = "A"
    # numRows = 1
    # result = "A"

    # solution.convert(s, numRows)
    print(solution.convert1(s, numRows))
    assert result == solution.convert1(s, numRows)
    # assert result == solution.convert2(s, numRows)
    assert result == solution.convert3(s, numRows)









