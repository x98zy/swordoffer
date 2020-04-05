"""题目描述
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所
有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所
有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。"""

#链接：https://www.nowcoder.com/practice/9be0172896bd43948f8a32fb954e1be1?tpId=13&tqId=11216&rp=4&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def __init__(self):
        self.cur_list=[]
    def Insert(self, num):
        # write code here
        self.cur_list.append(num)
        self.cur_list.sort()#此处不能用sorted(self.cur_list)因为sorted函数会返回一个新的列表
    def GetMedian(self,data):
        # write code here
        length=len(self.cur_list)
        if length%2==0:
            return (self.cur_list[length//2]+self.cur_list[length//2-1])/2.0
        else:
            return self.cur_list[int(length//2)]