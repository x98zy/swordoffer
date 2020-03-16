"""题目描述：在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每
个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输
入长度为7的数组{2,3,1,0,2,5,3}，
那么对应的输出是第一个重复的数字2。"""

#链接：https://www.nowcoder.com/practice/623a5ac0ea5b4e5f95552655361ae0a8?tpId=13&tqId=11203&tPage=3&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False
        flag=False
        count=0
        for i in range(len(numbers)-1):
            if numbers[i] in numbers[i+1:]:
                flag=True
                if count==0:
                    duplication[0]=numbers[i]
                    count+=1
        return flag