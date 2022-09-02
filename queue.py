# FIFO
# enqueue & dequeue

queue = []


def enqueue(elem):
    queue.append(elem)


def dequeue():
    queue.pop(0)


enqueue(1000)
enqueue(1001)
enqueue(1002)
enqueue(1003)
enqueue(1004)
enqueue(1005)
print(queue)

dequeue()
dequeue()
dequeue()
print(queue)
