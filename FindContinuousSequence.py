"""题目描述：小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是
100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,
他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列?"""

#链接：https://www.nowcoder.com/practice/c451a3fd84b64cb19485dad758a55ebe?tpId=13&tqId=11194&tPage=3&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if not tsum:
            return []
        res=[]
        for i in range(1,tsum):
            for j in range(i+1,tsum):
                start,end=i,j
                if (start+end)*(end-start+1)/2==tsum:
                    res.append([n for n in range(start,end+1)])
        return res