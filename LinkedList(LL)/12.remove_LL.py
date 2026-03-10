
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
    def get(self, index):
        if index < 0 or index >= self.length:  
            return None
        temp = self.head
        for _ in range(index):   
            temp = temp.next
        return temp 
    
    def pop(self):
        if self.length==0:          
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0:        
            self.head = None
            self.tail = None
        return temp.value                     

    def pop_first(self):
        if self.length==0:   
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        if self.length == 0:
            self.tail = None
        return temp.value

    def remove(self,index):                         #Remove node from middle
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        pre = self.get(index-1)              #prev:Specifying the location of a node before a node to be removed
        temp = pre.next                      #Make the previous node point to the node next to the one being removed
        pre.next = temp.next                 #Make the previous node create a connection with the next node after the middle one was removed
        temp.next = None                     #This detach completely and remove the node from the linnkedlist                 
        self.length-=1                       # Report the length of the list
        return temp
    

        

    
my_linked_list = LinkedList(20)

my_linked_list.append(22)
my_linked_list.append(24)
my_linked_list.append(21)

my_linked_list.remove(1)

my_linked_list.print_list()