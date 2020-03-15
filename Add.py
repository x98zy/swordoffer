"""题目描述：写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。"""
#链接：https://www.nowcoder.com/practice/59ac416b4b944300b617d4f7f111b215?tpId=13&tqId=11201&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def Add(self, num1, num2):
        # write code here
        if num1 is None or num2 is None:
            return -1
        while num2 != 0:
            sums = num1 ^ num2
            num2 = (num1&num2)<<1 # 进位
            num1 = sums & 0xFFFFFFFF # 考虑负数
        return num1 if num1 >> 31 == 0 else num1 - 4294967296