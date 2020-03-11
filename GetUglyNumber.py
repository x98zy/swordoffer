"""题目描述：把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数"""
#链接：https://www.nowcoder.com/practice/6aa9e04fc3794f68acf8778237ba065b?tpId=13&tqId=11186&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index<=0:
            return 0
        result=[1]
        p2=p3=p5=0
        for i in range(1,index):
            minnum=min(result[p2]*2,result[p3]*3,result[p5]*5)
            result.append(minnum)
            if result[i]==result[p2]*2:
                p2+=1
            if result[i]==result[p3]*3:
                p3+=1
            if result[i]==result[p5]*5:
                p5+=1
        return result[index-1]