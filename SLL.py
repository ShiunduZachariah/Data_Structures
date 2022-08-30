#Node
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


#head
class Sll:
    def __init__(self):
        self.head = None


a= Node(5)
b= Node(3)
c= Node(8)
d = Node(88)

sll = Sll()
sll.head = a
a.next = b
b.next = c
c.next = d

tmp = sll.head

while tmp is not None:
    print(tmp.data, end="->")
    if tmp.next is None:
        print("None")
    tmp = tmp.next

