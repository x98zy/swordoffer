"""题目描述：牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student.
 a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了
，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？"""
#链接：https://www.nowcoder.com/practice/3194a4f4cf814f63919d0790578d51f3?tpId=13&tqId=11197&tPage=3&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return ""
        res=[]
        j=0
        for i in range(len(s)):
            if s[i]==" ":
                res.append(s[j:i])
                j=i+1
        res.append(s[j:])
        start=0
        end=len(res)-1
        while start<=end:
            res[start],res[end]=res[end],res[start]
            start+=1
            end-=1
        return " ".join(res)