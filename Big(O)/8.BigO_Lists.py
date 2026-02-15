#Example1:
#Add a number at the end of the list
my_list = [11,3,23,7]
my_list.append(17)

#Notes: By adding 17 to end of the list, the index of each number in the list doesn't change

#Example 2:
# Remove a number from end of the list
my_list2 = [11,3,23,7,17]
my_list2.pop()

print(my_list)
print(my_list2)

#Notes: By removing 17 from the end of the list, the index of each number remain the same
#Both 1 & 2 are considered to be "O(1)""

#Example 3:
#Removing and the number at the beginning of the list

my_list3 = [11,3,23,7]
my_list3.pop(0)

my_list4 = [11,3,23,7]
my_list4.insert(0,17)

# Removing and adding at the begining make the ramining numbers acquire differnt index
# Because of that the is "O(n)"


my_list5 = [11,3,23,7]
my_list5.pop(1)

my_list6 = [11,3,23,7]
my_list6.insert(1,"Hi")

#Removing or adding something in the middle will cause the reindexing.
# This is also "O(n)"

print(my_list3)
print(my_list4)
print(my_list5)
print(my_list6)


#Printing 7 using iteration
my_list7= [11,3,23,7]

for item in my_list7:
    if item == 7:
        print(item)

#Print 7 using index iteration

for i in range(len(my_list7)):
    if my_list7[i] == 7:
        print("7 is present at the index of ",i)  

#Both iteration methods are "O(n)"

print(my_list7[-1])

#This method is "O(1)"




