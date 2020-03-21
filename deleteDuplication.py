"""题目描述：在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5"""

#链接：https://www.nowcoder.com/practice/fc533c45b73a41b0b44ccba763f866ef?tpId=13&tqId=11209&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None
        numlist=[]
        pre=pHead
        cur=pHead.next
        while cur:
            if cur.val==pre.val and cur.val not in numlist:
                numlist.append(cur.val)
            pre=cur
            cur=cur.next
        while pHead and pHead.val in numlist:
            pHead=pHead.next
        if pHead==None:
            return None
        pre=pHead
        cur=pHead.next
        while cur:
            if cur.val in numlist:
                pre.next=cur.next
                cur=cur.next
            else:
                pre=cur
                cur=cur.next
        return pHead

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None
        head=ListNode(0)
        head.next=pHead
        pre=head
        cur=pHead
        while cur:
            if cur.next and cur.val==cur.next.val:
                while cur.next and cur.val==cur.next.val:
                    cur=cur.next
                cur=cur.next
                pre.next=cur
            else:
                pre=cur
                cur=cur.next
        return head.next