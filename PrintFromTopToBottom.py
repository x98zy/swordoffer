"""题目描述：从上往下打印出二叉树的每个节点，同层节点从左至右打印。"""
#链接：https://www.nowcoder.com/practice/7fe2212963db4790b57431d9ed259701?tpId=13&tqId=11175&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root :
            return []
        if not root.left and not root.right:
            return [root.val]
        queue=[root]
        res=[]#返回结果
        while len(queue)!=0:
            copy=[avg for avg in queue]#此处不能直接赋值，否则copy和queue指向同一对象
            current=[]
            while len(copy)!=0:
                node=copy.pop(0)
                queue.pop(0)
                current.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res+=current
        return res


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:return ''
        queue = [root]
        res = []
        while queue:
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            res.append(queue[0].val)
            queue.pop(0)
        return res
"""本道题的解答技巧在于利用队列的先进先出的特性"""