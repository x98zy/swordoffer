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


