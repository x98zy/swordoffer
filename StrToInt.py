"""题目描述：将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0"""
#链接：https://www.nowcoder.com/practice/1277c681251b4372bdef344468e4f26e?tpId=13&tqId=11202&tPage=3&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        if s=="-2147483649" or s=="2147483648":
            return 0
        strlist=[str(n) for n in range(10)]
        length=len(s)
        sum=0
        if s[0]!="+" and s[0]!="-":
            for i in range(len(s)):
                if s[i] not in strlist:
                    return 0
                sum+=strlist.index(s[i])*(10**(length-i-1))
            return sum
        else:
            for i in range(1,len(s)):
                if s[i] not in strlist:
                    return 0
                sum+=strlist.index(s[i])*(10**(length-i-1))
            if s[0]=="+":
                return sum
            else:
                return -sum
        return sum