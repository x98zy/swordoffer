"""题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""
#链接https://www.nowcoder.com/practice/22243d016f6b47f2a6928b4313c85387?tpId=13&tqId=11162&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number==1:
            return 1
        return 2*self.jumpFloorII(number-1)

"""解题思路：由于青蛙每次可以选择从1到n中跳法，所以我们在第一次选择列举出所有的跳法
当n=1时，第一步只能跳一阶并且完成不需要再跳，当n=2时，第一步可以跳一阶也可以跳2阶
当第一步跳一阶时，此时只剩下一阶这相当与n=1的情况，当第一步跳2级时完成爬台阶了
当n=1时，sum=f(1),n=2时，sum=f(2)+f(1),f(n)表示第一步跳n阶，这样经我们推导当
n+1时，sum翻两倍"""
