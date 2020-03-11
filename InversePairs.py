"""题目描述：在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007"""
#链接：https://www.nowcoder.com/practice/96bd6684e04a44eb80e6a68efc0ec6c5?tpId=13&tqId=11188&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
class Solution:
    def __init__(self):
        self.count=0
    def MergeSort(self,lists):
        if len(lists)<=1:
            return lists
        mid=len(lists)//2
        left=self.MergeSort(lists[:mid])
        right=self.MergeSort(lists[mid:])
        return self.Merge(left,right)
    def Merge(self,left,right):
        l,r=0,0
        result=[]
        while l<len(left) and r<len(right):
            if left[l]<right[r]:
                result.append(left[l])
                l+=1
            else:
                result.append(right[r])
                r+=1
                self.count=self.count+len(left)-l
        result+=left[l:]
        result+=right[r:]
        return result
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0
        if len(data)==1:
            return 0
        self.MergeSort(data)
        return self.count%1000000007