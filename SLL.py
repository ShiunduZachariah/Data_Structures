# Node
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


# head
class Sll:
    def __init__(self):
        self.head = None


def add_element_beginning(Sll, newelem):
    n = Node(newelem)
    n.next = Sll.head
    Sll.head = n


def add_element_atlocation(Sll, newelement, location):
    tmp = Sll.head
    for i in range(location - 1):
        if tmp is not None:
            tmp = tmp.next
        else:
            print("Location is out of bound")
            break

    n = Node(newelement)
    nxt = tmp.next
    tmp.next = n
    n.next = nxt

def add_element_last(head, newelement):
    tmp = head
    while tmp.next is not None:
        tmp = tmp.next

    e = Node(newelement)
    tmp.next = e

def delete_elem(sll, element):
    tmp = sll.head
    if tmp.data == element:
        sll.head = tmp.next
        tmp= None
    else:
        while tmp is not None:
            if tmp.data == element:
                break
            bef = tmp
            tmp = tmp.next

        bef.next = tmp.next

def printlist(head):
    tmp = head
    while tmp is not None:
        print(tmp.data, end="->")
        if tmp.next is None:
            print("None")
        tmp = tmp.next

a = Node(5)
b = Node(3)
c = Node(8)
d = Node(88)

sll = Sll()
sll.head = a
a.next = b
b.next = c
c.next = d

printlist(sll.head)
add_element_beginning(sll, 100)
add_element_beginning(sll, 101)
add_element_atlocation(sll, 1000, 2)
add_element_last(sll.head, 99)

tmp = sll.head

printlist(sll.head)

delete_elem(sll, 101)
printlist(sll.head)