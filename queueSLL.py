class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


# head
class Sll:
    def __init__(self):
        self.head = None


# FIFO enqueue and dequeue methods
def enqueue(Sll, newelement):
    location = 1
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


def dequeue(sll):
    tmp = sll.head

    while tmp.next is not None:
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


queue = Sll()
H = Node("head")
queue.head = H
enqueue(queue, 101)
enqueue(queue, 102)
enqueue(queue, 103)
enqueue(queue, 104)
enqueue(queue, 105)
enqueue(queue, 106)
enqueue(queue, 107)
enqueue(queue, 108)

printlist(queue.head)

dequeue(queue)
printlist(queue.head)
dequeue(queue)
dequeue(queue)
dequeue(queue)
printlist(queue.head)

