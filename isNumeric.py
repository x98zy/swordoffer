"""题目描述：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。"""
#链接：https://www.nowcoder.com/practice/6f8c901d091949a5837e24bb82a731f2?tpId=13&tqId=11206&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s:
            return False
        numlist=[]
        if "e" in s:
            numlist=s.split("e")
        else:
            numlist=s.split("E")
        if "" in numlist:
            return False
        num=[str(n) for n in range(10)]
        flag=0
        for i in range(len(numlist[0])):
            if numlist[0][i]=="+" or numlist[0][i]=="-":
                if i!=0:
                    return False
            elif numlist[0][i]==".":
                flag+=1
                if flag>=2:
                    return False
                continue
            elif numlist[0][i] not in num:
                return False
        if len(numlist)>=2:
            for i in range(len(numlist[1])):
                if numlist[1][i]=="+" or numlist[1][i]=="-":
                    if i!=0:
                        return False
                elif numlist[1][i] not in num:
                    return False
        return True