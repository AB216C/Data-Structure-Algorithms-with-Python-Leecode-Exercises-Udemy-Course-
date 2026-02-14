class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length= 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self,value):                          #Method to append a new node at the end of the list
        new_node = Node(value)
        if self.head == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
    
    def prepend(self,value):                       #Method to add a node at the beginning of the list       
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    

my_linked_list = LinkedList(1)

my_linked_list.append(2)

my_linked_list.prepend(13)

my_linked_list.print_list()
