"""题目描述：输入一棵二叉树，判断该二叉树是否是平衡二叉树。"""
#链接：https://www.nowcoder.com/practice/8b3b95850edb4115918ecebdf1b4d222?tpId=13&tqId=11192&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        leftlen,rightlen=0,0
        if pRoot.left:
            leftlen=len(self.SeekDepth(pRoot.left))
        if pRoot.right:
            rightlen=len(self.SeekDepth(pRoot.right))
        if abs(leftlen-rightlen)<=1:
            return True
        return False
    def SeekDepth(self,root):
        queue=[root]
        res=[]
        while queue:
            current=[]
            i=0
            numflag=len(queue)
            while i<numflag:
                point=queue.pop(0)
                if point.val:
                    current.append(point.val)
                if point.left:
                    queue.append(point.left)
                if point.right:
                    queue.append(point.right)
                i+=1
            if len(current):
                res.append(current)
        return res