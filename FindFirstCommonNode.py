"""题目描述：输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的"""
#链接：https://www.nowcoder.com/practice/6ab1d9a29e88450685099d45c9e31e46?tpId=13&tqId=11189&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or  not pHead2:
            return None
        p1=pHead1
        p2=pHead2
        while p1!=p2:
            p1=p1.next
            p2=p2.next
            if p2!=p1:
                if p1==None:
                    p1=pHead2
                if p2==None:
                    p2=pHead1
        return p1