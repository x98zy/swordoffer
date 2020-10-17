"""题目描述：HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:
在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,
如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},
连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不
会被他忽悠住？(子向量的长度至少是1)"""
#链接：https://www.nowcoder.com/practice/459bd355da1549fa8a49e350bf3df484?tpId=13&tqId=11183&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return None
        if max(array)<=0:
            return max(array)
        res=[]
        for i in range(len(array)):
            res.append(self.Helper(array,i))
        return sorted(res)[-1]
    def Helper(self,array,start):
        end=0
        nagitive=0
        positive=0
        while start<len(array):
            if array[start]>0:
                positive=array[start]
                if positive+nagitive>0:
                    end=end+positive+nagitive
                    nagitive=0
            else:
                nagitive+=array[start]
            start+=1
        return end


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return None
        dp=[0 for i in range(len(array))]
        maxnum=array[0]
        dp[0]=array[0]
        for i in range(1,len(array)):
            newmax=dp[i-1]+array[i]
            if newmax>array[i]:
                dp[i]=newmax
            else:
                dp[i]=array[i]
            if dp[i]>maxnum:
                maxnum=dp[i]
        return maxnum