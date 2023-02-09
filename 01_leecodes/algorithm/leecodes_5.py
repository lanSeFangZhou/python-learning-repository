# https://leetcode.cn/problems/longest-palindromic-substring/
'''
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"


提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成
'''

# TODO
class Solution(object):
    def longestPalindrome(self, s):
        """
        时间复杂度：O(n^2)
        空间复杂度: O(n^2)
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j]是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由L和i可以确定右边界，即j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要dp[i][L] == true 成立，就表示子串s[i..L]是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin: begin + max_len]


    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1


    def longestPalindrome1(self, s: str) -> str:
        '''
        时间复杂度:O(n^2)
        空间复杂度:O(1)
        :param s:
        :return:
        '''
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end -start:
                start, end = left2, right2
        return s[start: end + 1]


        # def isPalindromeStr(input_str):
        #     input_str_len = len(input_str)
        #     if input_str_len % 2 == 0:
        #         for i in range(input_str_len):
        #             pass

if __name__ == "__main__":
    solution = Solution()
    s = "babad"
    s = "cbbd"
    print(solution.longestPalindrome(s))
    print(solution.longestPalindrome1(s))






