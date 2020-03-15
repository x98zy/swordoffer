"""题目描述：LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个
小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能
抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片
5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何
数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小
王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅
牌模拟上面的过程,然后告诉我们LL的运气如何，
 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。"""

#链接：https://www.nowcoder.com/practice/762836f4d43d43ca9deb273b3de8e1f4?tpId=13&tqId=11198&tPage=3&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        numbers.sort()
        if 0 in numbers:
            flag=0
            count=numbers.count(0)
            numbers=numbers[count:]
            i=0
            for i in range(len(numbers)-1):
                if numbers[i]==numbers[i+1]:
                    return False
                if numbers[i]!=numbers[i+1]-1:
                    num=numbers[i+1]-numbers[i]
                    flag+=num-1
            if flag>count:
                return False
            else:
                return True
        else:
            for i in range(len(numbers)-1):
                if numbers[i]!=numbers[i+1]-1:
                    return False
            return True

class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        numlist=[]
        num=0
        for i in range(len(numbers)):
            if numbers[i]==0:
                num+=1
            else:
                if numbers[i] not in numlist:
                    numlist.append(numbers[i])
        if num+len(numlist)!=5:
            return False
        if max(numlist)-min(numlist)<5:
            return True