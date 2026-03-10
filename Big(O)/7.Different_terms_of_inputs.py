def print_items(a,b):
    for i in range(a):
        print(i)                 # This marked as O(a)
    
    for j in range(b):
        print(j)                 # This is marked as O(b)

                                 # Both of them are marked as O(a+b)
                                 # n is not used here since the function has two differnt inputs


def print_items2(a,b):
    for i in range(a):          
        for j in range(b):
            print(i,j)         # This is marked as O(a*b)


print(print_items(5,10))
print(print_items2(5,10))

