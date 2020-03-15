"""每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自
然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让
编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并
且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下
去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。
请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)"""

#链接：https://www.nowcoder.com/practice/f78a359491e64a50bce2d89cff857eb6?tpId=13&tqId=11199&tPage=3&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not n:
            return -1
        s = 0
        for i in range(2, n+1):
            s = (s+m) % i
        return s

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not n:
            return -1
        strlist=[i for i in range(n)]
        cur=-1
        while len(strlist)>1:
            for i in range(m):
                cur+=1
                if cur==len(strlist):
                    cur=0
            strlist.pop(cur)
            cur-=1
        return strlist[0]