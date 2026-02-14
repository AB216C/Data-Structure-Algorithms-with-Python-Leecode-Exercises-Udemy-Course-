
class Cookie:
    def __init__(self,color):          # Constructure -- This will be used for cookie you may need to make
        self.color = color

        #Add some methods
    
    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color=color

    
cookie1 = Cookie("Green")
cookie2 = Cookie("Blue")

print("Cookie 1 is now ", cookie1.get_color())
print("Cookie 2 is now", cookie2.get_color())


cookie2.set_color("Yellow")

print("Cookie 1 is still", cookie1.get_color())
print("Cookie 2 been changed to ", cookie2.get_color())

## For data structure, class will be used as follows:

# class LinkedList:
#     def __init__(self, value):
#         self.value = value

#     def append(self, value):

#     def pop(self):

#     def prepend(self, value):

#     def insert(self, index, value):

#     def __init__(self, index):

