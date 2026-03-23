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
    def reverse(self):
        #Current status of the linkedlist
        prev = None
        current = self.head 
        while current:
            next_node = current.next
            #reversing the pointer
            current.next = prev
            # After reverse-this is the report:
            # Prev and current move forward, it is no longer, None, it becomes prev replace current while current move to the the next node
            prev = current
            current = next_node
        self.head = prev

    


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.print_list()
print("LIST BELOW IS REVERSED")
my_linked_list.reverse()
my_linked_list.print_list()