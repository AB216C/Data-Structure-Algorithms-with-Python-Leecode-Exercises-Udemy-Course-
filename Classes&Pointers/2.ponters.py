# From this example, num1 and num2 are pointing to the same boject in the memory
num1 = 11

num2 = num1

print("num1:", num1)
print("num2:", num2)

print("\nnum1 points to :", id(num1))
print("\nnum2 points to :", id(num2))

num2 = 22

print("num1:", num1)
print("num2:", num2)

print("\nnum1 points to :", id(num1))
print("\nnum2 points to :", id(num2))

# After updating num2, the num1 remained unchanged because integer are immutable
# Once the integer is created, it can not be changed.
#num2 and num1 are pointing to a differnt objects in memory because python created new integer object
# num2 is now pointed to a newly created object(22)

# DICTIONARIES

print("\nUnderstanding Pointers for Dictionary")

dict1 = {
    "value" : 11
}

dict2 = dict1


print("\ndict1 = :", dict1)
print("dict2 = ", dict2)

print("\ndict1 points to: ", id(dict1))
print("dict2 points to: ", id(dict2))

## CHANGING THE VALUE IN THE DICTIONARY

dict2['value'] = 22
print("\nHow dictionaries behave after changing the value")
print("\ndict1 = :", dict1)
print("dict2 = ", dict2)

print("\ndict1 points to: ", id(dict1))
print("dict2 points to: ", id(dict2))

# Since dictionaries are mutable, modifying the object through dict2 also affects dict1.
# dict1 and dict2 remain pointing to the same object in memory even after the value has been changed

## Garpage Collection process

dict3 = {
    "value":33
}

dict2 = dict3
    #and 
dict1 = dict2

# dict1, dict2, and dict3 will all point to the same node(33)
# Thus, value 11 and 22 will be removed by python under Garbage collection process

