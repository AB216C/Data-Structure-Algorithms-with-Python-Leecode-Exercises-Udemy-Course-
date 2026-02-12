def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(10)

# These print 100 items. 00 first item and 99 last item
# This is n*n = n^2  or O(n^2)

# on a graph, O(n^2) has a steeper line while O(n) is strait.
# For time complexity standpoint, O(n^2) is less efficient