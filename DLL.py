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

def add_element_beginning(Dll, newelem):
    n = Node(newelem)
    n.next = Dll.head
    Dll.head.prev = n
    Dll.head = n

def add_element_atlocation(Dll, newelement, location):
    temporary = Dll.head
    for i in range(location-1):
        if temporary is not None:
            temporary = temporary.next
        else:
            print("Location is out of bound")
        break

    n = Node(newelement)
    nxt = temporary.next
    temporary.next = n
    n.prev = temporary.next
    n.next = nxt
    nxt.prev = n


def add_element_last(head, newelement):
    tmp = head
    while tmp.next is not None:
        tmp = tmp.next

    e = Node(newelement)
    tmp.next = e
    e.prev = tmp

def delete_elem(dll, element):
    tmp = dll.head
    if tmp.data == element:
        dll.head = tmp.next
        tmp= None
    else:
        while tmp is not None:
            if tmp.data == element:
                break
            bef = tmp
            tmp = tmp.next

        bef.next = tmp.next
        tmp.next.prev = bef.next

def printlist(head):
    tmp = dll.head
    while tmp is not None:
        print(tmp.data, end="->")
        if tmp.next is None:
            print("None")
        tmp = tmp.next


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
add_element_beginning(dll, 100)
#add_element_atlocation(dll, 2, 3)





#add_element_atlocation(dll, 1000, 3)
printlist(dll.head)
add_element_last(dll.head, 99)
printlist(dll.head)

delete_elem(dll, 5)
printlist(dll)