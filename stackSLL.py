class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


# head
class Sll:
    def __init__(self):
        self.head = None


# stack push and pop
def pushstack(Sll, newelement, location):
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


def popstack(sll):
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


stack = Sll()
a = Node(99)
stack.head = a
printlist(stack.head)
pushstack(stack, 100, 1)
printlist(stack.head)

pushstack(stack, 101, 2)
pushstack(stack, 102, 3)
pushstack(stack, 103, 4)
pushstack(stack, 104, 5)

printlist(stack.head)
popstack(stack)
printlist(stack.head)
