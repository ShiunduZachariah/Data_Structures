# Node
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


root = Node(5)
a = Node(3)
b = Node(7)
c = Node(2)
d = Node(4)
e = Node(6)
f = Node(8)

root.left = a
root.right = b
a.left = c
a.right = d
b.left = e

print()


def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


insert(root, 3)
insert(root, 7)
insert(root, 8)
insert(root, 2)
insert(root, 2)
insert(root, 4)
insert(root, 6)


def inorder(root):  # left -> root -> right
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


print("\nInorder")
inorder(root)

print()


def preorder(root):  # root -> left -> right
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


print("\nPreorder")
preorder(root)

print()


def postorder(root):  # left -> right -> root
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


print("\nPostorder")
postorder(root)
