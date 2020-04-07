"""题目描述
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积
是多少？例如，当绳子的长度是8时，
我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。"""
#链接：https://www.nowcoder.com/practice/57d85990ba5b440ab888fc72b0751bf8?tpId=13&tqId=33257&rp=4&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def cutRope(self, number):
        # write code here
        if number<2:
            return 0
        if number==2:
            return 1
        if number==3:
            return 2
        return self.cutRoper(number)
    def cutRoper(self,number):
        if number<4:
            return number
        max_res=0
        for i in range(1,number/2+1):
            max_res=max(self.cutRoper(i)*self.cutRoper(number-i),max_res)
        return max_res


class Solution:
    def cutRope(self, number):
        # write code here
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2
            # 申请辅助空间
        products = [0] * (number + 1)
        # 定义前几个初始变量的值
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3
        # 进行动态规划,也就是从下向上的进行求解
        for i in range(4, number + 1):
            max_ = 0
            for j in range(1, i / 2 + 1):
                max_ = max(products[j] * products[i - j], max_)
            products[i] = max_

        max_ = products[number]
        return max_