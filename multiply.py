"""题目描述：给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素
B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。（注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，
B[n-1] = A[0] * A[1] * ... * A[n-2];）"""

#链接：https://www.nowcoder.com/practice/94a4d381a68b47b7a8bed86f2975db46?tpId=13&tqId=11204&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return []
        B=[]
        for j in range(len(A)):
            copy=A[:]
            copy.pop(j)
            B.append(self.mul(copy))
        return B
    def mul(self,lists):
        sum=1
        for i in range(len(lists)):
            sum*=lists[i]
        return sum

class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return []
        B=[1 for i in range(len(A))]
        res=1
        for i in range(len(A)):
            B[i]=res
            res*=A[i]
        res=1
        for j in range(len(A)-1,-1,-1):
            B[j]*=res
            res*=A[j]
        return B