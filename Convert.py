"""题目描述：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，
只能调整树中结点指针的指向。"""
#链接：https://www.nowcoder.com/practice/947f6eb80d944a84850b0538bf0ec3a5?tpId=13&tqId=11179&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def __init__(self):
        self.res=[]
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        self.MidSearch(pRootOfTree)
        if len(self.res)==1:
            self.res[0].left=None
            self.res[0].right=None
        else:
            self.res[0].left=None
            self.res[0].right=self.res[1]
            for i in range(1,len(self.res)):
                self.res[i].left=self.res[i-1]
                if i==len(self.res)-1:
                    self.res[i].right=None
                else:
                    self.res[i].right=self.res[i+1]
        return self.res[0]
    def MidSearch(self,root):
        if root.left:
            self.MidSearch(root.left)
        if root:
            self.res.append(root)
        if root.right:
            self.MidSearch(root.right)