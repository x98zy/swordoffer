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


class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        # 标记符号、小数点、e是否出现过
        sign = False
        decimal = False
        hasE = False
        for i in range(len(s)):
            if (s[i] == 'e' or s[i] == 'E'):
                # e后面一定要接数字
                if (i == len(s)-1):
                    return False
                # 不能同时存在两个e
                if (hasE == True):
                    return False
                hasE = True
            elif (s[i] == '+' or s[i] == '-'):
                # 第二次出现+-符号，则必须紧接在e之后
                if (sign and s[i-1] != 'e' and s[i-1] != 'E'):
                    return False
                # 第一次出现+-符号，且不是在字符串开头，则也必须紧接在e之后
                elif (sign == False and i > 0 and s[i-1] != 'e' and s[i-1] != 'E'):
                    return False
                sign = True
            elif (s[i] == '.'):
                # e后面不能接小数点，小数点不能出现两次
                if (hasE or decimal):
                    return False
                decimal = True
            # 非法字符
            elif(s[i] < '0' or s[i] > '9'):
                return False
        return True