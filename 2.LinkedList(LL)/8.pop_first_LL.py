#Removing the node the beginning

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
    def append(self,value):                                  #Method to append a new node
        new_node = Node(value)
        if self.head == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    def pop_first(self):
        if self.length==0:           #Checking the Length of a list before declement
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        if self.length == 0:
            self.tail = None
        return temp.value


my_linked_list = LinkedList(1)
my_linked_list.append(2)

# 2 items - Return 1 Node

print(my_linked_list.pop_first())

#  1 item - Return 2 Node 

print(my_linked_list.pop_first())

# 0 item - Return 0 Node

print(my_linked_list.pop_first())