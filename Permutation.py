"""题目描述：输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba"""
#链接：https://www.nowcoder.com/practice/fe6b651b66ae47d7acce78ffdd9a96c7?tpId=13&tqId=11180&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        res=[]
        def helper(ss,tmp):
            if not ss:
                res.append(tmp)
                return
            else:
                for i in range(len(ss)):
                    helper(ss[0:i]+ss[i+1:],tmp+ss[i])
        helper(ss,"")
        return sorted(list(set(res)))