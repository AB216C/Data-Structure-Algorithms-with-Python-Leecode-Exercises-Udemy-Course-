def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for k in range(n):
        print(k)

print_items(10)

# This is can be written as O(n^2 + n); but n is dropped and remain with O(n^2)

