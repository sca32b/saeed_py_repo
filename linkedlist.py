#Singly linked list implementation
from random import randint

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_Node = Node(data)
        if not self.head:
            self.head = new_Node
            self.tail = self.head
        else:
            self.tail.next = new_Node
            self.tail = new_Node
        self.length += 1
        return self

mylist = LinkedList(10)
listofnodes = []

for i in range(10):
    print(mylist)
    print(mylist.length)
    mylist.append(randint(1,100))
    print(mylist.length)
    print(mylist.tail)
    listofnodes.append(mylist.tail)

print(f"The length of the list is {mylist.length}")
print(f"The list of nodes is {listofnodes}")

# traverse the linkedlist

current = mylist.head
for i in range(mylist.length):
    print(current.data)
    current = current.next