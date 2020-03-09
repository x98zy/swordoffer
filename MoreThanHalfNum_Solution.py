"""题目描述：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。"""
#链接：https://www.nowcoder.com/practice/e8a1b01a2df14cb2b228b30ee6a92163?tpId=13&tqId=11181&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        if len(numbers)==1:
            return numbers[0]
        count=1
        prevalue=numbers[0]
        for i in range(1,len(numbers)):
            if numbers[i]==prevalue:
                count+=1
            else:
                count-=1
            if count==0:
                prevalue=numbers[i]
                count=1
        num=0
        for i in range(0,len(numbers)):
            if numbers[i]==prevalue:
                num+=1
        return prevalue if num>len(numbers)//2 else 0