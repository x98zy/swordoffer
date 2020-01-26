"""题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。"""
#链接 https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=13&tqId=11161&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

"""解题思路：
如果台阶书n=1,那么跳跃方式只有一种，如果台阶数n=2,那么跳跃方式有2中，为1，1和2
我们知道跳上n阶台阶只有可能只有两种情况，分别是从跳一个台阶到n阶台阶和跳2阶台阶到n阶台阶
最后总结出跳到n阶台阶的可能方案是调到n-1阶方案和n-2阶方案之和"""
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number<=2:
            return number#台阶数小于2直接返回
        pre1,pre2=2,#pre1是跳到n-1阶台阶的方案，n-2是跳到n-2阶台阶数的方案
        for i in range(3,number+1):
            cur=pre1+pre2
            pre2=pre1
            pre1=cur
        return cur
