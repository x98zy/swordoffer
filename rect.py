"""我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的
大矩形，总共有多少种方法？
"""
#链接：https://www.nowcoder.com/practice/72a5a919508a4251859fb2cfb987a0e6?tpId=13&tqId=11163&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
class Solution:
    def rectCover(self, number):
        # write code here
        if number==0:
            return 0
        if number==1 or number==2:
            return number
        pre1,pre2=2,1
        for i in range(3,number+1):
            sum=pre2+pre1
            pre2=pre1
            pre1=sum
        return sum



