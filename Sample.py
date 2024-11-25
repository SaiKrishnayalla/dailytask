text = " Hello, world! "
print(text.strip())   # Output: "Hello, World!"
print(text.lstrip())  # Output: "Hello, World!   "
print(text.rstrip())  # Output: "   Hello, World!"

text1=text.replace(" ","")
print(text1)
text2=text.replace("Hello"," ")
print(text2)
text3=text.replace("Hello","Happpyyyy")
print(text3)

print("_____________________________________")
class Dog:

    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))