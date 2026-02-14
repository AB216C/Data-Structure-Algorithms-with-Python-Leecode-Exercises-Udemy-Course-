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

    def print_list(self,value):
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

    def pop(self):
        if self.length==0:           #Checking the Length of a list before declement
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0:         #Checking the Length of a list after declement
            self.head = None
            self.tail = None
        return temp.value             #This return the removed node
    


my_linked_list = LinkedList(1)
my_linked_list.append(2)


# 2 items - Return 2 Node

print(my_linked_list.pop())

#  1 item - Return 1 Node 

print(my_linked_list.pop())

# 0 item - Return 0 Node

print(my_linked_list.pop())
    





