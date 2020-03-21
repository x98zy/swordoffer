"""题目描述：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，
同时包含指向父结点的指针。"""

class Solution:
    def __init__(self):
        self.listnode=[]
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        p=pNode
        while p.next:
            p=p.next
        self.MidSearch(p)
        for i in range(len(self.listnode)):
            if pNode==self.listnode[i]:
                if i==len(self.listnode)-1:
                    return None
                else:
                    return self.listnode[i+1]
    def MidSearch(self,node):
        if node:
            self.MidSearch(node.left)
            self.listnode.append(node)
            self.MidSearch(node.right)