"""给定一个有环链表，实现一个算法返回环路的开头节点。
有环链表的定义：在链表中某个节点的next元素指向在它前面出现过的节点，则表明该链表存在环路。"""
#https://leetcode-cn.com/problems/linked-list-cycle-lcci/

class Solution():
    def detectCycle(self,head):
        if not head or head.next==head:
            return head
        node1,node2=head,head.next
        steps=[]
        while node1 and node2:
            if node2 in steps:
                return node2
            steps.append(node1)
            steps.append(node2)
            node1=node1.next
            node2= node2.next

class Solution():
    def detectCycle(self,head):
        fast,slow=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                break
        if not fast or not fast.next:
            return None
        fast=head
        while fast!=slow:
            fast=fast.next
            slow=slow.next
        return fast
range()
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


