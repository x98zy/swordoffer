"""编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list-lcci"""

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        left,right=[],[]
        phead=head
        while phead:
            if phead.val<x:
                left.insert(0,phead)
            else:
                right.insert(0,phead)
            phead=phead.next
        for i in range(len(left)):
            if i==len(left)-1:
                left[i].next=None
            else:
                left[i].next=left[i+1]
        for j in range(len(right)):
            if j==len(right)-1:
                right[j].next=None
            else:
                right[j].next=right[j+1]
        if len(right)==0:
            return left[0]
        if len(left)==0:
            return right[0]
        else:
            left[len(left)-1].next=right[0]
            return left[0]

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        p,q=head,head
        while q:
            if q.val<x:
                p.val,q.val=q.val,p.val
                p=p.next
            q=q.next
        return head