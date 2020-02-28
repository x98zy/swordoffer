"""题目描述：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）"""
#链接：https://www.nowcoder.com/practice/6e196c44c7004d15b1610b9afca8bd88?tpId=13&tqId=11170&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
class Solution:
    def __init__(self):
        self.res1=[]
        self.res2=[]
    def MidSearch1(self,pRoot):
        if pRoot.left:
            self.MidSearch1(pRoot.left)
        if pRoot:
            self.res1.append(pRoot.val)
        if pRoot.right:
            self.MidSearch1(pRoot.right)
    def MidSearch2(self,pRoot):
        if pRoot.left:
            self.MidSearch2(pRoot.left)
        if pRoot:
            self.res2.append(pRoot.val)
        if pRoot.right:
            self.MidSearch2(pRoot.right)
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2==None or pRoot1==None:
            return False
        self.MidSearch1(pRoot1)
        self.MidSearch2(pRoot2)
        set1=set(self.res1)
        set2=set(self.res2)
        if set2&set1==set2:
            return True
        return False