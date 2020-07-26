"""给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的 深拷贝。 

我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/copy-list-with-random-pointer"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        phead=Node(head.val)
        rthead=phead
        node_list1=[head]
        node_list2=[rthead]
        stored_node=head
        head=head.next
        while head:
            link_node=Node(head.val)
            node_list1.append(head)
            node_list2.append(link_node)
            phead.next=link_node
            phead=link_node
            head=head.next
        p=rthead
        while p:
            if stored_node.random:
                index=node_list1.index(stored_node.random)
                p.random=node_list2[index]
            else:
                p.random=None
            p=p.next
            stored_node=stored_node.next
        return rthead

class Solution(object):
    def __init__(self):
        self.pathdict={}
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        node=Node(head.val)
        if head in self.pathdict:
            return self.pathdict[head]
        else:
            self.pathdict[head]=node
        node.next=self.copyRandomList(head.next)
        node.random=self.copyRandomList(head.random)
        return node