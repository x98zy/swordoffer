"""题目描述大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39"""
#链接https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

#方法一
class Solution:
    def Fibonacci(self, n):
        # write code here
        Fib=[0,1]
        if n>39:
            return
        elif n<=1:
            return Fib[n]
        else:
            return self.Fibonacci(n-2)+self.Fibonacci(n-1)
#此种算法的时间复杂度为2的n次方，空间复杂度为O(1)

#方法二
class Solution:
    def Fibonacci(self, n):
        # write code here
        Fib=[0,1]
        if n>39:
            return
        for i in range(2,40):
            Fib.append(Fib[i-1]+Fib[i-2])
        return Fib[n]

#此种算法的时间复杂度为O(n)但空间复杂度为O(n)

#方法三
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n<=1:
            return 0 if n==0 else 1
        one=1
        two=0
        sum=0
        for i in range(2,n+1):
            sum=one+two
            two=one
            one=sum
        return sum
#此种算法的原理是我们只用打了最近的两个数所以只需两个变量来存储刷新即可，再用sum返回，时间复杂度O(n),空间复杂度O(1)

#方法四
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n<=1:
            return 0 if n==0 else 1
        one=0
        sum=1
        for i in range(2,n+1):
            sum=sum+one
            one=sum-one
        return sum
#时间复杂度O(n),空间复杂度O(1)