# A node is made up two elements
     #1. Value
     #2. Pointer

# Secondly, a node is a dictionary

# Example of a node with a value of 12 

node = {
    "value" : 12,
    "next": None
}

# This is how a Linked List Look like under the hood

# 11 -> 3 -> 23 -> 7 -> 4

head = {
    "value": 11,
    "next": {
        "value": 3,
        "next" : {
            "value": 23,
            "next":{
                "value": 7,
                "next": {
                    "value": 4,                # ==> tail 
                    "next": None
                }
            }
        }
    }
}

#Printing the values fromt he LinkedList
print(head['next']['value'])
print(head['next']['next']['value'])
print(head['next']['next']['next']['value'])

# The print code below will only work with LinkedList

# print(my_linked_list.head.next.next.value)
