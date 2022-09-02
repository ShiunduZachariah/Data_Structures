# LIFO
# Push & pop
stack = []


def pushstack(elem):
    stack.append(elem)


def popstack():
    stack.pop()


pushstack(1000)
pushstack(1001)
pushstack(1002)
pushstack(1003)
pushstack(1004)
pushstack(1005)

print(stack)


popstack()
popstack()
popstack()
print(stack)

pushstack(999)
print(stack)