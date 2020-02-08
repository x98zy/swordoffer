"""输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示"""
#https://www.nowcoder.com/practice/8ee967e43c2c4ec193b040ea7fbb10b8?tpId=13&tqId=11164&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n<0:
            n=n&0xffffffff
        return bin(n).count("1")
#方式二
@
class Solution():
    def NumberOf1(self, n):
        if n<0:
            n=n&0xffffffff
        count=0
        while n:
            count+=1
            n=n&(n-1)
