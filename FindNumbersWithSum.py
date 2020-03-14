"""题目描述：输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的"""
#链接：https://www.nowcoder.com/practice/390da4f7a00f44bea7c2f3d19491311b?tpId=13&tqId=11195&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        if len(array)==1:
            return []
        res=[]
        start=0
        end=len(array)-1
        while end>start:
            if array[start]+array[end]<tsum:
                start+=1
            elif array[start]+array[end]>tsum:
                end-=1
            else:
                res.append([array[start],array[end]])
                start+=1
                end-=1
        if len(res)==1:
            return res[0]
        elif len(res)==0:
            return []
        else:
            minnum=res[0][0]*res[0][1]
            index=0
            for i in range(1,len(res)):
                if res[i][0]*res[i][1]<=minnum:
                    minnum=res[i][0]*res[i][1]
                    index=i
            return res[index]