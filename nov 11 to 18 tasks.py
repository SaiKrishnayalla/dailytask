x= int(input("Enter a nuber:"))
print(type(x))
print("________________________") 
"""nov 12 2024 task examples//"""
X=10
print(type(X))
y=10
print(type(y))
print(X+y)
print(X**y)
print(X-y)
print(X%y)
print("___________________________") 
""" nov 13 2024 task examples//"""
A=1.44
B=14+15j
print(type(A))
print(type(B))
print("_____________________________")

x=int(input("enter a number:"))
i=1
while i<10:
    print(x,"*",i,"=",i*x)
    i=i+1

print("_____________________________________")
"""contional statements examples"""
Q=20
if Q>=20:
    print("Q is is grater than 20")
else:
    print("Q is less thane 20")
print("______________________________________")
print("welcome to atm")
pin=int(input("enter your 6 digit pin number:"))
amount = 1000000
if (pin==112233):
    print("Welocme")
    print("1. withdraw")
    print("2. deposite")
    print("3. balance enquiry")
    choice= int(input("please choose your option:"))
else:
    print("wrong pin")
if (choice ==1):
    x=int(input("enter with draw amount")) 
    print("withdraw successfull")
    amount=int(input("enter the amount:"))
if amount<5000:
    print("you have withdrawn")
if (choice==2):
    y=int(input("enter deposite amount"))
    print("deposite to your account successful")
if(choice==3):
    print("your savings account balance is",amount)
    print("thank you")
else:

    print("wrong pin")
print("__________________________________________")
x=int(input("enter the number:"))
i=1
while i<10:
    i=i+1
    print(x,"X",i,"=",i*x)
print("____________________________________________")
m=1
for m in range(10):
    m=m+1
    print(m)
print("_______________________________________")
set=[11,12,13,14,15,16]
print(set)