#Drop Constants

def print_items(n):
    for i in range(n):
        print(i)


    for j in range(n):
        print(j)

print_items(10)

# since n + n = 2n, doesn't mean, we have O(2n). Constant is dropped and still write O(n)
