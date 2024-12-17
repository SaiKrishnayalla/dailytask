#Write a program to create a set.
set = {1,2,3,"vamsi",True,11,1,2,3,1,4,5,6,7}
print(type(set))
print(set)

#Write a python program to iterate over sets.
set = {1,2,3,"vamsi",True,11,1,2}
if "vamsi" in set:
    print("vamsi is present in the set")
else:
    print("vamsi is not present in the set")


#Write a Python program to add member to a set.
set = {1,2,3,"vamsi",True,11,1,2}
set.add(4)
print(set)

#Write a Python program to remove a member from a set.
set = {1,2,3,"vamsi",True,11,1,2}
set.remove(1)
print(set)

#Write a Python program to remove item from a given set.
set = {1,2,3,"vamsi",True,11,1,2}
set.remove(2)
print(set)
set.discard("vamsi")
print(set)
#Write a python program to create a intersection of set ?
set_1 = {"sun","mon","tue","wed","thur"}
set_2 = {"tue","wed","sat","holiday"}
print(set_1.intersection(set_2))
print(type(set_1))
print(type(set_2))

#Write a python program to createa unionof set ?'
set_1 = {"sun","mon","tue","wed","thur"}
set_2 = {"tue","wed","sat","holiday"}
print(set_1.union(set_2))

#Write a python program to create set differance ?
set_1 = {1,2,3,4,5,6}
set_2 = {10,11,1,2,3,4,5,6}
print(set_1.difference(set_2))

#Write a Python program to remove items 10, 20, 30 from the following set at once.?
set = {1,2,3,4,5,6,7,8,9,"vvv",10,20,30}
set.discard(10)
set.discard(20)
set.discard(30)
print(set)


#Check if two sets have any elements in common. If yes, display the common elements?
set_1 = {1,2,3,4,5,6}
set_2 = {10,11,1,2,3,4,5,6}
print(set_1.intersection(set_2))

#Update set1 by adding items from set2, except common items?
#Remove items from set1 that are not common to both set1 and set2?


                                      
#Write a python program to  add a key to a dictionary ?
dict = {
    "date":17,
    "time":4

}
dict['day'] = "tuesday"
print(dict)
#Write a python program to check weather the given value is present in the dictionary or not ?
dict = {
    "name":"vamsi",
    "age": 22,
    "city":"hyd"
}
if "name" in dict:
    print("yes")
    if "age" in dict:
        print("yes")
#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
#Write a python program to create a dictionary from the string ?
#Write a python program to combine two dictionaries by adding values of common keys ?

#Write a python program to merge two python dictionaries ?
dict_1 = {
    "name":"vamsi",
    "company":"skywaves"
 }
dict_2 = {
    "Uan created": "NO",

    "mail id": "vamsi@gmail.com"

}
dict_3 = dict_1 | (dict_2)
print(dict_3)
#Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.
#Sample string : 'skywavessoftwares'
#Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
