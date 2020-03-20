"""题目描述：请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配"""
#链接：https://www.nowcoder.com/practice/45327ae22b7b413ea21df13ee7d6429c?tpId=13&tqId=11205&tPage=3&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if not s and not pattern:
            return True
        len1=len(s)
        len2=len(pattern)
        dp=[[False]*(len2+1) for i in range(len1+1)]
        dp[0][0]=True
        for m in range(1,len2+1):
            if m>=2 and pattern[m-1]=="*":
                dp[0][m]=dp[0][m-2]
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                m,n=i-1,j-1
                if pattern[n]=="*":
                    if s[m]==pattern[n-1] or pattern[n-1]==".":
                        dp[i][j]=dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j]=dp[i][j-2]
                elif s[m]==pattern[n] or pattern[n]==".":
                    dp[i][j]=dp[i-1][j-1]
        return dp[len1][len2]