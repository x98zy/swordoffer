"""题目描述：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。"""
#https://www.nowcoder.com/practice/a861533d45854474ac791d90e447bafd?tpId=13&tqId=11176&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def __init__(self):
        self.num=0
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence)==0 and self.num!=0:
            return True
        if len(sequence)!=0:
            left=[sequence[i] for i in range(len(sequence)-1) if sequence[i]<sequence[-1]]
            right=[sequence[i] for i in range(len(sequence)-1) if sequence[i]>sequence[-1]]
            self.num+=1
            if left+right+[sequence[-1]]==sequence:
                return self.VerifySquenceOfBST(left) and self.VerifySquenceOfBST(right)
        else:
            return False
