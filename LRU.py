class Node():
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None

class TwoWayList():
    def __init__(self):
        self.head=None
        self.tail=None
        self._length=0

    def IsEmpty(self):
        return self._length==0

    @property
    def length(self):
        return self._length

    def Insert_Head(self,node):
        head=self.head
        self._length+=1
        if head:
            node.next=head
            self.head=node
            node.prev=None
            head.prev=node
        else:
            self.head=self.tail=node
            node.next=node.prev=None

    def pop(self):
        if self._length==0:
            return None
        tail=self.tail.prev
        tail.next=None
        self.tail.prev=None
        self.tail=tail
        self._length-=1
        return

    def remove(self,node):
        if self._length==0:
            return
        if self._length==1:
            self.head=self.tail=None
        if node==self.head:
            head=self.head.next
            self.head.next=None
            head.prev=None
            self.head=head
        elif node==self.tail:
            tail=self.tail.prev
            tail.next=None
            self.tail.prev=None
            self.tail=tail
        else:
            node.prev.next=node.next
            node.next.prev=node.prev
            node.next=None
            node.prev=None
        self._length-=1

class LRU():
    def __init__(self,cap):
        self.table={}
        self.TwoLinkList=TwoWayList()
        self.size=0
        self.cap=cap

    def get(self,node):
        key=node.key
        if key in self.table:
            node=self.table[key]
            self.TwoLinkList.remove(node)
            self.TwoLinkList.Insert_Head(node)
            return node
        return None

    def set(self,node):
        key=node.key
        if key in self.table:
            _node=self.table[key]
            self.table[key]=node
            self.TwoLinkList.remove(_node)
            self.TwoLinkList.Insert_Head(node)
            self.size+=1
        else:
            if self.size==self.cap:
                self.TwoLinkList.pop()
                del self.table[self.TwoLinkList.tail.key]
                self.TwoLinkList.pop()
                self.size-=1
            self.TwoLinkList.Insert_Head(node)
            self.size+=1
            self.table[node.key]=node