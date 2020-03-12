"""题目描述：统计一个数字在排序数组中出现的次数"""
#链接：https://www.nowcoder.com/practice/70610bf967994b22bb1c26f9ae901fa2?tpId=13&tqId=11190&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        def getfirst(data,k):
            left=0
            right=len(data)-1
            while right>=left:
                if data[left]==k:
                    return left
                mid=(left+right)//2
                if data[mid]>k:
                    right=mid-1
                elif data[mid]<k:
                    left=mid+1
                else:
                    if mid>0:
                        if data[mid]==k and data[mid-1]!=k:
                            return mid
                        else:
                            right=mid-1
            return -1
        def getlast(data,k):
            left=0
            right=len(data)-1
            while right>=left:
                if data[right]==k:
                    return right
                mid=(left+right)//2
                if data[mid]>k:
                    right=mid-1
                elif data[mid]<k:
                    left=mid+1
                else:
                    if mid<len(data)-1:
                        if data[mid]==k and data[mid+1]!=k:
                            return mid
                        else:
                            left=mid+1
            return -1
        first=getfirst(data,k)
        last=getlast(data,k)
        if first>-1 and last>-1:
            return last-first+1
        return 0