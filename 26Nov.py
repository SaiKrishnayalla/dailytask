#1.Python Program to count occurrence of a given characters in string.
a = "hello guys how are you hope you are doing well"
count = a.count('h')
print(count)
#2.Python Program to check if two Strings are Anagram. 
text = "hello        world"
y=text.replace(" ","")
print(y)
#5.Python program to replace the string space with a given character using replace() method.
text = " h e l l o w o r l d"
y=text.replace(" ","")
print(y)
#6.Python program to convert lowercase char to uppercase of string.
x= "hello today and tomorrow are holidays"
y=x.upper()
print(y)


#8.Python program to separate characters in a given string.
x= "python"
y=x.split()
print(y)

#9.Python program to remove blank space from string.
x="   some batch people are not getting           salaries     "
y=x.replace("    ","")
y=x.replace(" ","")
print(y)
#10. Python program to concatenate two strings using join() method.
x="hello"
y="world"
print(x.join(y))
 
#11. Python program to concatenate two strings without using join() method.
x="hello"
y="world"
print(x+y)
#12. Python program to remove repeated character from string.



#13. Python program to check given character is vowel or consonant. 
x="i"
if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
    print("vowel")
else:
    print("consonant")

x="v"
if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
    print("vowel")
else:
    print("consonant")

#14. Python program to check given character is digit or not.
#  
x= "1234567890"
print(x.isdigit())

#15. Python program to delete vowels in a given string. 
string ="hello world"
y=string.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
print(y)
#16. Python program to count the Occurrence Of Vowels & Consonants in a String. 
x = "learning python is easy"
vowels = "aeiou"
consonents = "bcdfghjklmnpqrstvwxyz"
x1=sum(x.count(vowels)for vowels in vowels)
x2=sum(x.count(consonents)for consonents in consonents)
print()
print(x1)
#17. Python program to print the highest frequency character in a String. 

#18. Python program to Replace First Occurrence Of Vowel With ‘-‘ in String. 

#19. Python program to count alphabets, digits and special characters. 

#20. Python program to check given character is digit or not using isdigit() method. 

#21. Python program to calculate sum of integers in string. 
a =12
b=34
c=56
d=11
e=100
print(a+b+c+d)
#22. Python program to print all non repeating character in string. 

#23. Python program to copy one string to another string.
x = "bewbf"
y= x
print(x)
print(y)

#24. Python program to check given character is vowel or consonant.
x="i"
if (x=='a' or x=='e'or x=='i' or x=='o' or x=='u'):
   print("vowel")
else:
   print("consonant")

#25. Python program to check given character is digit or not.
x= "1234567890"
print(x.isdigit())
