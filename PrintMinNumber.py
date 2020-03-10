"""题目描述：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。"""
#链接：https://www.nowcoder.com/practice/8fecd3f8ba334add803bf2a06af1b993?tpId=13&tqId=11185&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        for i in range(0,len(numbers)-1):
            for j in range(i+1,len(numbers)):
                sum1=str(numbers[i])+str(numbers[j])
                sum2=str(numbers[j])+str(numbers[i])
                if int(sum1)>int(sum2):
                    numbers[i],numbers[j]=numbers[j],numbers[i]
        res=""
        for num in numbers:
            res+=str(num)
        return int(res)