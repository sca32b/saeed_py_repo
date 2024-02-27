class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def append(self, value):
        new_node = Node(value)
        if not self.head:
            print("First element created")
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

list = SinglyLinkedList()
list.append("15")
print(list.head.data)