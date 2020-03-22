"""题目描述：从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。"""

#链接：https://www.nowcoder.com/practice/445c44d982d04483b04a54f298796288?tpId=13&tqId=11213&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        queue=[pRoot]
        res=[]
        while queue:
            current=[]
            i=0
            flag=len(queue)
            while i<flag:
                point=queue.pop(0)
                current.append(point.val)
                if point.left:
                    queue.append(point.left)
                if point.right:
                    queue.append(point.right)
                i+=1
            if current:
                res.append(current)
        return res