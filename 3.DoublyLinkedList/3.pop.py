class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1
        return True
    #After declement
    # def pop(self):
    #     if self.length == 0:
    #         return None
    #     temp = self.tail
    #     self.tail = self.tail.prev
    #     temp.prev = None
    #     self.length -= 1
    #     if self.length == 0:
    #         self.head = None
    #         self.tail = None
    #     return temp
    
    #After decelement is written in a different way
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            temp.prev = None
        self.length -= 1
        return temp.value

doublylinkedlist = DoublyLinkedList(3)
doublylinkedlist.append(200)

print(doublylinkedlist.pop())
print(doublylinkedlist.pop())
print(doublylinkedlist.pop())


# doublylinkedlist.print_list()