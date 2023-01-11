'''
https://leetcode.cn/problems/longest-substring-without-repeating-characters/
3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。



示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
'''

import logging as log

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_len = len(s)
        str_list = s.split()
        start_index = 0
        end_index = 0
        while True:
            if (end_index < str_len and \
                s[start_index:end_index] != s[end_index:(end_index+end_index-start_index)]) \
                or (start_index == end_index):
                end_index += 1
            else:
                start_index = end_index
            print(f"start_index:{start_index}")
            print(f"end_index:{end_index}")
            if end_index == str_len - 1:
                break
        return s[start_index:end_index]


    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        print(f"lookup:{lookup}")
        print(f"result:{s[cur_len:cur_len+max_len]}")
        return max_len



if __name__ == "__main__":
    solution = Solution()
    s = "abcabcbb"
    result = solution.lengthOfLongestSubstring1(s)
    # log.info(f"result:{result}")
    print(f"result:{result}")


# 您的出生年月：1992年2月
# 户籍：陕西省安康市
# 目前薪资：年包53W+10W期权
# 期望薪资：年包65W左右
# 政治面貌：群众
# 到岗周期：随时
# 还有学历国内都可以认证吗：本科，211，可以的
# 还有离职原因是：公司和部门有大的变动，想要更好的长期发展机会












