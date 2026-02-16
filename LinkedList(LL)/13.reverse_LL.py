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
    def append(self,value):                        
        new_node = Node(value)
        if self.head == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
    def reverse(self):
        temp = self.head
        self.head = self.tail         #Switching head with tail first
        self.tail = temp
        after = temp.next             #At index ZERO, the node is made of three variables before, temp, and after
        before = None
        for _ in range(self.length):      #This iterate the entire node untill they are pointing backward
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    
my_linked_list = LinkedList(20)

my_linked_list.append(22)
my_linked_list.append(24)
my_linked_list.append(21)

my_linked_list.reverse()
my_linked_list.print_list()