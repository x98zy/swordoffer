"""题目描述：请实现一个函数，用来判断一颗二叉树是不是对称的。注意，
如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。"""

#链接：https://www.nowcoder.com/practice/ff05d44dfdb04e1d83bdbdab320efbcb?tpId=13&tqId=11211&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        queue=[pRoot]
        res=[]
        while queue:
            current=[]
            flag=len(queue)
            i=0
            while i<flag:
                point=queue.pop(0)
                if point!=" ":
                    current.append(point.val)
                    if point.left:
                        queue.append(point.left)
                    else:
                        queue.append(" ")
                    if point.right:
                        queue.append(point.right)
                    else:
                        queue.append(" ")
                else:
                    current.append(" ")
                i+=1
            if current:
                res.append(current)
        for node in res:
            if node!=node[::-1]:
                return False
        return True

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return  self.Juge(pRoot,pRoot)
    def Juge(self,node1,node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val!=node2.val:
            return False
        return self.Juge(node1.left,node2.right) and self.Juge(node1.right,node2.left)