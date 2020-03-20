"""题目描述：请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。"""

#链接https://www.nowcoder.com/practice/00de97733b8e4f97a3fb5c680ee10720?tpId=13&tqId=11207&tPage=3&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    # 返回对应char
    def __init__(self):
        self.s=""
        self.dict={}
    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.dict[i]==1:
                return i
        return "#"
    def Insert(self, char):
        # write code here
        self.s+=char
        if char in self.dict:
            self.dict[char]+=1
        else:
            self.dict[char]=1