"""indexing in python"""
name = "Till now we have completed Pyton Basics"
print(name[0])
print(name[-1]) 
print(name[2])
print(name[10]) # count staring from 0 i;e- from first character

"""slicing a string"""
string = "Hell0,World"
print(string[0:5])
print(string[6:11])
print(string[0:11:2]) # start:stop:step
print(string[0:11:3])
print("___________________________________________")
String= "i phone 15"
print(String[1])
print(String[0:9:2])

"""membership checking with strings"""
X="Sai krishna owned a Thar"
print("Thar" in X)
print("Thar" not in X)
print("Sai" in X)
print("vamsi" in X)

""" Removing Spaces from string"""
text = "   Hello, World!   "
print(text.strip())   # Output: "Hello, World!"
print(text.lstrip())  # Output: "Hello, World!   "
print(text.rstrip())  # Output: "   Hello, World!"  
