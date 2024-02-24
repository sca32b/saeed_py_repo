
from random import randint

def enqueue(queue, item):
    queue.insert(0,item)
    return queue

def dequeue(queue):
    return queue.pop()

queue = []

for i in range(10):
    enqueue(queue, randint(1,100))

print(f"The length of the queue is {len(queue)}")
print(queue)

for i in range(len(queue)):
    print(dequeue(queue))

print(f"The length of the queue is {len(queue)}")