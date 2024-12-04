#1
x = [1,2,3,4,5]
y =sum(x)
print(y)
#2
fruits = ["apple","kiwi","mango","durrain","custerd apple"]
print(fruits[2])
print(fruits[4])
#3
list = [1,2,3,4,5,6,7,8,9,10]
print(list[:3])
print(list[-3:])
print(list[3:10:2])
#4
a= [10,20,30,40,50,60,70,80]
b= [90,100,110]
a.append(b)
print(a)
a1=a.insert(30,120)
print(a1)######
#5
num1= [2,4,6,8,10,12]
num2 = [3,5,7,9,11,13]
num1.extend(num2)
print(num1)
#line 10
#pop()
x=[1,2,3,4,5,3,6,7,3]
y=x.pop(8)
print(x)
#sort()
x=[11,44,22,7,1,3,2,4,8,43]
x.reverse()
print(x)
x.sort()
print(x)
x.sort(reverse = True) #decending order
print(x)

#revrse() and slicing
x=[10,11,12,13,14,15,16]
x.reverse()
print(x)
x[::-1]
print(x)
#aliasing and cloning
a=[1,2,3]
b=a
b[1] = 0
print(b)





#mathematical operators
l1=[21,22,23,24,25,26]
l2=[31,32,33,34,35,36]
l3 =l1+l2
print(l3)
print(l2*3)

#Given a list of numbers, write a Python program to create a new list where each element is doubled (i.e., each elementis multiplied by 2)



#Write a Python program to check if a specific element (e.g., 5) exists in a given list using the in operator. If it exists, print its position; otherwise, print "Element not found."
given = [1,2,3,4,5,6]
if 5 in given:
    print(given.index(5))
else:
    print("element not found")

#Given a list of student names, check if "John" and "Sara" are in the list using the in operator.
student = ["vamsi","sai","john","sara","venkatanandam"]
print("john"and "sara" in student)
#7. Nested Lists:
#1.Write a Python program to create a 3x3 matrix (nested list) and print the matrix. Then, access and print the element at row 2, column 3.


#2.Create a nested list representing a list of students' names and their respective grades. Write a Python program to print each student's name along with their grade.


#8. Advanced Challenges:


#1.Create a list of numbers from 1 to 20. Write a Python program to generate two separate lists:


#One containing only the even numbers.


#Another containing only the odd numbers.


#.Write a Python program that reads a list of integers and returns a new list containing only the unique elements (i.e., removing duplicates).



#iven a list of tuples representing (name, age), sort the list by age in ascending order.