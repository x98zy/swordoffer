"""题目描述：输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则"""
#链接：https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337?tpId=13&tqId=11169&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
#自己的代码
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1==None:
            return pHead2
        if pHead2==None:
            return pHead1
        temp=ListNode(0)
        head=temp
        n=1
        while pHead1 or pHead2:
            if pHead1 and pHead2:
                if pHead1.val>=pHead2.val and n==1:
                    temp.val=pHead2.val
                    pHead2=pHead2.next
                    n+=1
                elif pHead1.val<=pHead2.val and n==1:
                    temp.val=pHead1.val
                    pHead1=pHead1.next
                    n+=1
                elif pHead1.val>=pHead2.val and n!=1:
                    temp1=ListNode(pHead2.val)
                    pHead2=pHead2.next
                    temp.next=temp1
                    temp=temp.next
                elif pHead1.val<=pHead2.val and n!=1:
                    temp1=ListNode(pHead1.val)
                    temp.next=temp1
                    pHead1=pHead1.next
                    temp=temp.next
            if pHead1 and not pHead2:
                temp1=ListNode(pHead1.val)
                pHead1=pHead1.next
                temp.next=temp1
                temp=temp.next
            if pHead2 and not pHead1:
                temp1=ListNode(pHead2.val)
                pHead2=pHead2.next
                temp.next=temp1
                temp=temp.next
        return head
#代码改进
def Merge(self, l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

def Merge(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.Merge(l1.next, l2)
        return l1
    else:
        l2.next = self.Merge(l1, l2.next)
        return l2

def Merge(self, pHead1, pHead2):
    # write code here
    if pHead1 and pHead2:
        if pHead1.val > pHead2.val:
            pHead1, pHead2 = pHead2, pHead1
        pHead1.next = self.Merge(pHead1.next, pHead2)
    return pHead1 or pHead2
