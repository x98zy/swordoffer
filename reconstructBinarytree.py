"""牛客网剑指offer--重建二叉树："""
"""题目描述：
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例
如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}
，则重建二叉树并返回。"""
class TreeNode:#二叉树节点定义
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre)==0:
            return None
        if len(pre)==1:
            node=TreeNode(pre[0])#此处是一个易错点，不能直接返回pre[0]
            return node
        else:
            root=TreeNode(0)
            root.val=pre[0]
            index=tin.index(root.val)
            prel=pre[1:index+1]
            tinl=tin[0:index]#根节点的左森林
            prer=pre[index+1:len(pre)]
            tinr=tin[index+1:len(tin)]#根节点的右森林
            root.left=self.reConstructBinaryTree(prel,tinl)
            root.right=self.reConstructBinaryTree(prer,tinr)
            return root