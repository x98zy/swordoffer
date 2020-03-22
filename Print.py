"""题目描述：请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。"""

#链接：https://www.nowcoder.com/practice/91b69814117f4e8097390d107d2efbe0?tpId=13&tqId=11212&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        queue=[pRoot]
        res=[]
        while queue:
            flag=len(queue)
            i=0
            current=[]
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
        flagnum=1
        for i in range(len(res)):
            if flagnum==1:
                 flagnum=-1
            elif flagnum==-1:
                res[i]=res[i][::-1]
                flagnum=1
        return res