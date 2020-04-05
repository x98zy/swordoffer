"""题目描述
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，
如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动
窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的
滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
{2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。"""

#链接：https://www.nowcoder.com/practice/1624bc35a45c42c0bc17d17fa0cba788?tpId=13&tqId=11217&rp=4&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def maxInWindows(self, num, size):
        # write code here
        res=[]
        if size>len(num) or size==0:
            return []
        copy=num[0:size]
        res.append(max(copy))
        index=0
        count=0
        for i in range(size,len(num)):
            res.append(max(num[i-size+1:i+1]))
        return res