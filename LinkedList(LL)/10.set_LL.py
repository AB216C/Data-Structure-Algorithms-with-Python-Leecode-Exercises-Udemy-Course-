# Change a value of a node 

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
        return temp                         # (Return temp) only is needed since get methods is going to be used inside the set_value method
    
    def set_value(self, index, value):
        temp = self.get(index)                  # Another method inside a new method will Helps to return None or a node         
        if temp:
            temp.value = value
            return True
        return False

my_linked_list = LinkedList(30)

my_linked_list.append(20)
my_linked_list.append(15)
my_linked_list.append(50)

my_linked_list.set_value(1,5)
my_linked_list.print_list()