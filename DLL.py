# Node
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        self.prev = None


# head
class Dll:
    def __init__(self):
        self.head = None


a = Node(5)
b = Node(3)
c = Node(8)
d = Node(88)

dll = Dll()
dll.head = a
a.next = b
b.prev = a
b.next = c
c.prev = b
c.next = d
d.prev = c

tmp = dll.head

while tmp is not None:
    print(tmp.data, end="->")
    if tmp.next is None:
        print("None")
    tmp = tmp.next

tmpLast = d

while tmpLast is not None:
    print(tmpLast.data, end="<-")
    if tmpLast.prev is None:
        print("Head")
    tmpLast = tmpLast.prev
