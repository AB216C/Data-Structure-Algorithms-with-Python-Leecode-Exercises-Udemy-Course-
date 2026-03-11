# O of 1=Constant time(As n increases, the number of operations will remain constant)
# On grapth, the line is flat on x-axis

def add_items(n):
    return n

def add_items2(n):
    return n + n


def add_items3(n):
    return n + n + n

print(add_items(1))
print(add_items2(1))
print(add_items3(1))

#Explanations: For 2nd and 3rd function, though, it becomes 2n or 3n, the big O  drops constant
#              Instead of being 2(1) or 3(1) becomes O(1)