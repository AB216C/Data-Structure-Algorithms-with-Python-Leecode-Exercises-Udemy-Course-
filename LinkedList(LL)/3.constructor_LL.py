
# Creating a new Nodes using constructor

# This is creating Nodes constructure
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# Creating LinkedList Constructure

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
print(my_linked_list.tail.value)

