#1.Write a function that takes a tuple and an index as inputs and returns the element at the given index. Handle the case where the index is out of bounds.
#tup = input("Enter tuple value")




#2.Write a function to concatenate two tuples into one.
t1 = (1,2,3,4,5,6)
t2  = (7,8,9,10,11)
tuple = t1 + t2
print(t1)


#3.Write a function that takes a tuple and a value as inputs and returns the number of times the value appears in the tuple.
def my_function(tuple):
    li = []
    for i in tuple:
        suv = tuple.count(i)
        if i in li:
            continue
        else:

tuple = input("Enter the value:")
my_function(tuple)


#4.Write a function that calculates the length of a tuple without using the built-in `len()` function.





#5.Write a function that takes a tuple as input and returns a new tuple with the elements in reverse order.
tuple_1 = (100,10)
tuple_2 = tuple_1[::-1]
print(tuple_2)




#8.Write a function that takes a tuple as input and returns a new tuple with the elements in reverse order.





#9.Write a function that checks if a given element exists in a tuple. Return `True` if it exists, otherwise return `False`.
tup = (10, 4, 5, 6, 8)
x = 6
for ele in tup:
    if x == ele:
        result = True
        break
else:
    result = False
print( str(result))




#10.Write a function that takes two tuples and returns a tuple containing the common elements.






#11.Write a function to unpack nested tuples and flatten them into a single tuple.  
#    Example:  
 #   Input: `((1, 2), (3, 4), 5)`  
  #  Output: `(1, 2, 3, 4, 5)`

