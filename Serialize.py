"""题目描述：请实现两个函数，分别用来序列化和反序列化二叉树
二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某
格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存
序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，
序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。
二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树"""

#链接：https://www.nowcoder.com/practice/cf7e25aa97c04cc1a68c8f040e71fb84?tpId=13&tqId=11214&tPage=4&rp=4&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def __init__(self):
        self.index=-1
    def Serialize(self, root):
        # write code here
        if not root:
            return "#"
        return str(root.val)+","+self.Serialize(root.left)+","+self.Serialize(root.right)
    def Deserialize(self, s):
        # write code here
        if not s:
            return None
        p=s.split(",")
        p=[n for n in p if n!=" "]
        self.index+=1
        if self.index>=len(s):
            return
        treenode=None
        if p[self.index]!="#":
            treenode=ListNode(int(p[self.index]))
            treenode.left=self.Deserialize(s)
            treenode.right=self.Deserialize(s)
        return treenode