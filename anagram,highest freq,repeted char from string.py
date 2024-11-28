#2.  Python Program to check if two Strings are Anagram.
n1 = str(input("Enter the first string2: "))
n2 = str(input("Enter the second string2: "))

if (sorted(n1) == sorted(n2)):
    print("n1 and n2 are anagrams")
else:
    print("n1 and n2 are not anagrams")
#12. Python program to remove repeated character from string.
x='qqbbccddffbbhh'
y=''
for element in x:
     if element  not in y:
          y=y+element
          print(element)
#17. Python program to print the highest frequency character in a String.
str= input("Enter a string17:")
l = list(str)
freq = {}
for i in l:
     if i in freq:
          freq[i] +=1
else:
    freq[i]=1
#18. Python program to Replace First Occurrence Of Vowel With ‘-‘ in String. 
n1 = input("Enter the source string18: ")
vowels ='aeiouAEIOU'
for i in n1:
        if i in vowels:
            n1 = n1.replace(i, '-', 1)  # Replace first occurrence of vowel
            break                       # Exit the loop after replacing the first vowel
print(n1)
#19. Python program to count alphabets, digits and special characters. 

#20. Python program to check given character is digit or not using isdigit() method. 
n1 = input("Enter a character20: ")
 
if (n1.isdigit()):
    print(" n1 is a digit ")
else:
    print(" n1 is not a digit ")
#21. Python program to calculate sum of integers in string.
s = "vamsi12345"
count = 0
for char in s:
    if char.isdigit():
        count = count + int(char)
    else :
        pass
print(count)
 
 
#22. Python program to print all non repeating character in string.
s =" welcome to my world"
nc = ""
for char in s:
    if char not in nc:
        nc = nc + char
print(nc)