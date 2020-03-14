"""题目描述：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字"""
#链接：https://www.nowcoder.com/practice/e02fdb54d7524710a7d664d082bb7811?tpId=13&tqId=11193&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def FindNumsAppearOnce(self, array):
        # write code here

        # 将组内元素异或，返回异或后的结果
        def XORarray(array):
            result = 0
            for i in range(len(array)):
                result ^= array[i]
            return result

        # 从低到高找到第一位为1的数
        # 与1(01)按位与&，0&1=0 0&0=0 1&0=0 1&1=1
        # 如果结果是0,则与2(10)按位与,直到找到让结果是1的theNum
        def getFirstBitIs1(num):
            theNum = 0
            while num & theNum == 0:
                theNum += 1
            return theNum

        num = XORarray(array)
        firstBitNum = getFirstBitIs1(num)
        result = [0, 0]
        # 分组进行异或
        for i in range(len(array)):
            if array[i] & firstBitNum == 0:
                result[0] ^= array[i]
            else:
                result[1] ^= array[i]
        return result
