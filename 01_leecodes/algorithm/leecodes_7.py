'''
https://leetcode.cn/problems/reverse-integer/
7. 整数反转
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0

提示：
-231 <= x <= 231 - 1
'''


class Solution(object):
    def reverse(self, x):
        """
        t:O(n)
        s:O(1)
        :type x: int
        :rtype: int
        """
        x = str(x)
        flag = False
        if x.startswith("-"):
            flag = True
            x = x[1:]

        result = ''
        if str(x).isdigit():
            for i in range(len(x)):
                result += [s for s in x][len(x) - i - 1]
            result = int(result)
            if flag:
                result = -result
            print(result)
            if -2 ** 31 <= result <= 2 ** 31 - 1:
                return result
            else:
                return 0
        else:
            print("包含非数字!")


    def reverse(self, x:int) -> int:
        '''
        t: O(log|x|)
        s: O(1)
        :param x:
        :return:
        '''
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        rev = 0
        while  x != 0:
            # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
                return 0
            digit = x % 10
            # python3 的取模运算在 x 为负数时也会返回[0, 9]以内的结果，因此这里需要进行特殊判断
            if x < 0 and digit > 0:
                digit -= 10

            # 同理，python3 的整数除法在 x 为负数时会向下(更小的负数) 取整, 因此不能写成 x //= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit
        return rev







if __name__ == "__main__":
    solution = Solution()
    x = 123
    result = 321
    assert result == solution.reverse(x)

    x = -123
    result = -321
    assert result == solution.reverse(x)

    x = 120
    result = 21
    assert result == solution.reverse(x)

    x = 0
    result = 0
    assert result == solution.reverse(x)

