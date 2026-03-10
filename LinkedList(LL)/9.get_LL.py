# Getting a node a cartain index

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
    def append(self,value):                         #Method to append a new node
        new_node = Node(value)
        if self.head == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
    def get(self, index):
        if index < 0 or index >= self.length:   #Linked list doesn't accept negative index such as -1, -2 or index out of range.
            return None
        temp = self.head
        for _ in range(index):                 #Notice the variable i was not used but underscore was used(_)
            temp = temp.next
        return temp.value                      # (Return temp) : Will only return a node(<__main__.Node object at 0x10395f320>). But (return temp.value) will return the value of the node
    

my_linked_list = LinkedList(30)

my_linked_list.append(20)
my_linked_list.append(15)
my_linked_list.append(50)

print(my_linked_list.get(2))