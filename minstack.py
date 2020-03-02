"""题目描述：定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法"""
#链接：https://www.nowcoder.com/practice/4c776177d2c04c2494f2555c9fcc1e49?tpId=13&tqId=11173&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
#自己的方案
class Solution:
    def __init__(self):
        self.stack=[]
        self.min_index=0
    def push(self, node):
        if len(self.stack)==0:
            self.stack.append(node)
            self.min_index=0
        else:
            self.stack.append(node)
            if node<self.stack[self.min_index]:
                self.min_index=self.stack.index(node)
    def pop(self):
        if self.min_index==len(self.stack)-1:
            num=min(self.stack[0:len(self.stack)-1])
            self.min_index=self.stack[0:len(self.stack)-1].index(num)
        self.stack.pop(-1)
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.stack[self.min_index]