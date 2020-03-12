"""题目描述：输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。"""
#链接：https://www.nowcoder.com/practice/435fb86331474282a3499955f0a41e8b?tpId=13&tqId=11191&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        queue=[pRoot]
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
        return len(res)