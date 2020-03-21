"""题目描述：给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null"""

#链接：https://www.nowcoder.com/practice/253d2c59ec3e4bc68da16833f79a38e4?tpId=13&tqId=11208&tPage=3&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None
        listnode=[pHead]
        while pHead:
            if pHead.next!=None and pHead.next not in listnode:
                listnode.append(pHead.next)
                pHead=pHead.next
            else:
                return pHead.next
        return None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None
        fast=pHead
        slow1=pHead
        while fast and fast.next:
            fast=fast.next.next
            slow1=slow1.next
            if fast==slow1:
                slow2=pHead
                while slow2!=slow1:
                    slow1=slow1.next
                    slow2=slow2.next
                return slow2
        return None