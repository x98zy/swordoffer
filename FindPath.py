"""输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开
始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)"""
#链接：https://www.nowcoder.com/practice/b736e784e3e34731af99065031301bca?tpId=13&tqId=11177&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.onepath=[]
        self.result=[]
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        self.onepath.append(root.val)
        expectNumber-=root.val
        if expectNumber==0 and not root.left and not root.right:
            self.result.append(self.onepath[:])#此处必须插入onepath的副本，否则最后最后插入的只是空列表
        elif expectNumber>0:
            if root.left:
                self.FindPath(root.left,expectNumber)
            if root.right:
                self.FindPath(root.right,expectNumber)
        self.onepath.pop(-1)
        self.result.sort(key=len)
        return self.result[::-1]