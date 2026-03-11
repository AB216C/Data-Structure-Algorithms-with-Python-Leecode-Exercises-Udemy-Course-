
#Order to append, you need to have constructor of a node, Constructor of a linked list, print List method, and append method

# This is creating Nodes constructure
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


# Creating LinkedList Constructure

class LinkedList:
    def __init__(self,value):                                #LinkedList contructor
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):                                    #Method to print values
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):                                  #Method to append a new node
        new_node = Node(value)
        if self.head == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.print_list()