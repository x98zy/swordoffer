"""题目描述：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）"""
#链接：https://www.nowcoder.com/practice/f836b2c43afc4b35ad6adc41ec941dba?tpId=13&tqId=11178&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        node=[]#存储节点
        relation={}#关系映射列表
        temp=pHead
        while pHead:
            node.append(pHead)
            pHead=pHead.next
        index=0
        for i in range(len(node)):
            if node[i].random:
                relation[i]=node.index(node[i].random)
            else:
                relation[i]=None
        pRetHead=RandomListNode(node[0].label)
        res=pRetHead
        node2=[pRetHead]
        for i in range(1,len(node)):
            singlenode=RandomListNode(node[i].label)
            pRetHead.next=singlenode
            pRetHead=pRetHead.next
            node2.append(singlenode)
        for j in range(len(node2)):
            if relation[j]:
                node2[j].random=node2[relation[j]]
            else:
                node2[j].random=None
        return res

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if  not pHead:
            return None
        node=pHead
        while node:
            newnode=RandomListNode(node.label)
            newnode.next=node.next
            node.next=newnode
            node=node.next.next
        node=pHead
        while node:
            newnode=node.next
            if node.random==None:
                newnode.random=None
            else:
                newnode.random=node.random.next
            node=node.next.next
        node=pHead
        res=pHead.next
        while node:
            newnode=node.next
            node.next=node.next.next
            if newnode.next:
                newnode.next=newnode.next.next
            else:
                newnode.next=None
            node=node.next
        return res