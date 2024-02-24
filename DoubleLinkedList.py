from random import randint

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList():
    def __init__(self, data):
        self.data = data
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_Node = Node (data)

        if not self.head:
            self.head = new_Node
            self.tail = self.head
        else:
            self.tail.next = new_Node
            new_Node.prev = self.tail
            self.tail = new_Node
        self.length += 1
        return self
    
mylist  = DoubleLinkedList(10)
for i in range(20):
        mylist.append(randint(1,100))
print(f"The length of the list is {mylist.length}")

current = mylist.head
for i in range(mylist.length):
        print(current.data)
        current = current.next
