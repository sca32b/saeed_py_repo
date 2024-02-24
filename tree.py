
from random import randint

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)
        self.length = 1

    def insert(self, data):
        new_Node = Node(data)
        print(new_Node.data)
        if not self.root:
            self.root = new_Node
            return self
        current = self.root
        while True:
            if data < current.data:
                if not current.left:
                    current.left=new_Node
                    self.length += 1
                    return self
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = new_Node
                    self.length += 1
                    return self
                else:
                    current = current.right

    def contains(self, data):
        current = self.root
        print(current.data)
        while current:
            if data == current.data:
                return True
            if data < current.data:
                current = current.left
                if current:
                  print(current.data)
            else:
                current = current.right
                if current:
                  print(current.data)
        return False

    def remove(self, data, start=None, parent=None):
       current = start or self.root
       while current and current.data != data:
           parent = current
           if data < current.data:
               current = parent.left
           else:
               current = parent.right
       if not current:
            return False
       if not current.left and not current.right:
           return self.remove_node_with_no_children(current, parent)
       if current.left and current.right:
            return self.remove_node_with_two_children(current, parent)
       return self.remove_node_with_one_child(current, parent)
    

    def remove_node_with_no_children(self, current, parent):
        if current == self.root:
            self.root = None
            return True
        if parent.left == current:
            parent.left = None
        else:
            parent.right = None
        return True
    
    def remove_node_with_one_child(self, current, parent):
        if current == self.root:
            self.root = current.left if current.left else current.right
            return True
        if current.left:
            parent.left = current.left if current.left else current.right
        else:
            parent.right = current.left if current.left else current.right
        return True

    def remove_node_with_two_children(self, current, parent):
        successor = locate_successor(current, parent)
        current.data = successor.data
        return self.remove(successor.data, start=current.right, parent=current)

    @staticmethod
    def locate_successor(current):
        successor = current.right
        while successor.left:
            parent = successor
            successor = successor.left
        return successor

'''   
        def remove(self, data):
        current = self.root
        parent = None
        if current.data == data:
            # remove the root
            print("Found the node")
        else:
            while current:

                if data < current.data:
                    parent = current
                    current = current.left
                else:
                    parent = current
                    current = current.right
                if not current:
                    return False
                elif current.data == data:
                    # remove the node if no child node
                    print("Found the node")
                    if not current.left and not current.right:
                        if parent.left == current:
                            parent.left = None
                        else:
                            parent.right = None
                    elif not current.left:
                        if parent.left == current:
                            parent.left = current.right
                        else:
                            parent.right = current.right
                    elif not current.right:
                        if parent.left == current:
                            parent.left = current.left
                        else:
                            parent.right = current.left
                    break
'''

my_tree = BinaryTree(10)
for i in range(60):
    my_tree.insert(randint(1,100))
print(f"The length of the tree is {my_tree.length}")

print(my_tree.contains(18))
print(my_tree.remove(18))


