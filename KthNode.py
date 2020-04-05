"""题目描述：给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）中，
按结点数值大小顺序第三小结点的值为4"""
#链接：https://www.nowcoder.com/practice/ef068f602dde4d28aab2b210e859150a?tpId=13&tqId=11215&tPage=4&rp=4&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.cur_list=[]
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot:
            return None
        self.LeftSearch(pRoot)
        if k>len(self.cur_list)or k==0:
            return None
        return self.cur_list[k-1]
    def LeftSearch(self,pRoot):
        if not pRoot:
            return None
        if pRoot.left:
            self.LeftSearch(pRoot.left)
        if pRoot:
            self.cur_list.append(pRoot)
        if pRoot.right:
            self.LeftSearch(pRoot.right)